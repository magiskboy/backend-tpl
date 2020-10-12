# coding=utf-8

from {{cookiecutter.pkg_name}}.model import Base
from tests import BaseTestCase


class BaseModelTestCase(BaseTestCase):
    def setUp(self):
        class Product(Base):
            pass
        self.model_cls = Product

    def test_class_model_config(self):
        assert self.model_cls.__tablename__ == self.model_cls.__name__.lower()
        assert hasattr(self.model_cls, 'id_')
