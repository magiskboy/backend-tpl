FROM python:3.8-alpine3.12 AS compile-image

LABEL maintainer="nguyenkhacthanh244@gmail.com" version="0.0.1"

WORKDIR /app

RUN apk update --no-cache && \
    apk add --no-cache make gcc g++ musl-dev

ADD ./requirements.txt .

RUN python -mvenv venv && \
    venv/bin/pip install cython && \
    venv/bin/pip install -r requirements.txt

FROM python:3.8-alpine3.12

ARG PORT=8000
ENV PORT=$PORT

WORKDIR /app

COPY --from=compile-image /app/venv ./venv

ADD . .

EXPOSE $PORT

ENTRYPOINT PYTHONPATH=. venv/bin/gunicorn {{cookiecutter.pkg_name}}.__main__:app \
    --worker-class=uvicorn.workers.UvicornWorker \
    --workers=$(nproc) \
    --bind="0.0.0.0:$PORT" \
    --log-level=error

CMD /bin/sh
