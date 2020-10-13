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

docker-build: {{cookiecutter.pkg_name}} Dockerfile .dockerignore
	docker build . -t {{cookiecutter.registry_repo}}:m-$(TAG)

docker-push:
	docker push {{cookiecutter.registry_host}}/{{cookiecutter.registry_repo}}:m-$(TAG)

clean:
	@rm -rf \
		coverage.xml \
		.coverage \
		htmlcov \
		*.egg-info \
		dist \
		docs/build \
		docs/source/refs
