TAG = $(shell cat .git/refs/heads/master | cut -c1-8)

all: dev

deps:
	pip install -r requirements-dev.txt

dev: deps
	python {{cookiecutter.pkg_name}} dev

test: deps
	python -m pytest

lint: deps
	PYTHONPATH=. python linter.py --fail-under 9.5 {{cookiecutter.pkg_name}}
	PYTHONPATH=. mypy {{cookiecutter.pkg_name}}

docker-build: Dockerfile .dockerignore
	docker build . -t {{cookiecutter.docker_repo_url}}:m-$(TAG)

clean:
	@rm -rf \
		coverage.xml \
		.coverage \
		htmlcov \
		*.egg-info \
		dist \
		docs/build \
		docs/source/refs