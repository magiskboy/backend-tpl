TAG = $(shell cat .git/refs/heads/master | cut -c1-8)
REGISTRY_IMAGE = {{cookiecutter.registry_repo}} 
REGISTRY_HOST = {{cookiecutter.registry_host}}
WORKERS = $(shell nproc)

# setup port in production
ifeq ($(strip ${PORT}),)
PORT = 8000
endif

all: dev

deps: requirements.txt requirements-dev.txt
	@pip install -r requirements-dev.txt > /dev/null

web: deps
	PYTHONPATH=. python app dev

job: deps
	PYTHONPATH=. celery -A app.core.celery:app worker \
		--loglevel=error

test: deps
	PYTHONPATH=. pytest

lint: deps
	PYTHONPATH=. python linter.py --fail-under 9.5 app
	PYTHONPATH=. mypy {{cookiecutter.pkg_name}}

docker-build: Dockerfile .dockerignore
	docker build . --build-arg PORT=$(PORT) -t $(REGISTRY_IMAGE):m-$(TAG)

docker-run:
	docker run -it --rm -p$(PORT):$(PORT) $(REGISTRY_IMAGE):m-$(TAG)

docker-push: docker-build
	docker push $(REGISTRY_HOST)/$(REGISTRY_IMAGE):m-$(TAG)

clean:
	@rm -rf \
		coverage.xml \
		.coverage \
		htmlcov \
		*.egg-info \
		dist \
