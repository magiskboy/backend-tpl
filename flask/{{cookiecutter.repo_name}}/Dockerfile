FROM python:3.8-alpine3.12 AS compile-image

LABEL maintainer="{{cookiecutter.author_email}}" version="{{cookiecutter.version}}"

WORKDIR /app

RUN apk update --no-cache && \
    apk add --no-cache make gcc musl-dev libffi-dev

ADD ./requirements.txt .

RUN python -mvenv venv && \
    venv/bin/pip install -r requirements.txt

FROM python:3.8-alpine3.12

WORKDIR /app

COPY --from=compile-image /app/venv ./venv

ADD . .

EXPOSE 8000

ENTRYPOINT PYTHONPATH=. venv/bin/gunicorn -c gunicorn.conf.py {{cookiecutter.pkg_name}}.wsgi:app

CMD /bin/sh
