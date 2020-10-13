TAG = $(shell cat .git/refs/heads/master | cut -c1-8)

all: dev

deps:
	pip install -r requirements-dev.txt

dev: deps
	FLASK_ENV=development FLASK_APP={{cookiecutter.pkg_name}}.api:create_app flask run

test: deps
	python -m pytest

lint: deps
	PYTHONPATH=. python linter.py --fail-under 9.5 flask_boilerplate
	PYTHONPATH=. mypy flask_boilerplate

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
