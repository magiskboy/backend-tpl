# coding=utf-8

from sqlalchemy.ext.declarative import declared_attr        #type:ignore
from sqlalchemy import (    #type:ignore
    Column,
    Integer
)
from flask_sqlalchemy import SQLAlchemy as BaseSQLAlchemy       #type:ignore
from flask_migrate import Migrate       #type:ignore


class SQLAlchemy(BaseSQLAlchemy):
    def init_app(self, app):
        super().init_app(app)
        Migrate(app, self)


db = SQLAlchemy()


class Base(db.Model):       #type:ignore
    __name__ = 'Base'

    id_ = Column('id', Integer(), primary_key=True)

    @declared_attr
    def __tablename__(cls) -> str:      # pylint:disable=E0213
        return cls.__name__.lower()     # pylint:disable=E1101
