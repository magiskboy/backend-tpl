# coding=utf-8

import pytest
from {{cookiecutter.pkg_name}} import api
from {{cookiecutter.pkg_name}}.model import (
    Base,
    db,
)


@pytest.fixture
def flask_client(request):
    app = None
    if request.cls is not None:
        app = api.create_app('testing')
        request.cls.app = app
        request.cls.client = app.test_client()
    yield app


@pytest.fixture
def database(request):
    app = api.create_app('testing')
    with app.app_context():
        Base.metadata.create_all(db.engine)
        yield
