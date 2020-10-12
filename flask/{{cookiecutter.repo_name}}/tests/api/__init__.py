# coding=utf-8

import pytest
from flask import Flask
from flask import testing
from tests import BaseTestCase


@pytest.mark.usefixtures('flask_client')
class APITestCase(BaseTestCase):
    app: Flask
    client: testing.FlaskClient
