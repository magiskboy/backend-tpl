# coding=utf-8

import typing as T
from {{cookiecutter.pkg_name}}.model import (
    db,
    Base as DbBaseModel,
)


class CRUDBase:
    def __init__(self, model: T.Type):
        self.model: T.Type = model

    def get(self, oid: int) -> T.Union[DbBaseModel, None]:
        return db.session.query(self.model).get(oid)

    def get_multi(self, offset: int = 0, limit: int = 10,
                  lazy: bool = True) -> T.List[DbBaseModel]:
        query = db.session.query(self.model).offset(offset).limit(limit)
        if lazy:
            return query
        return query.all()

    def create(self, data: T.Dict[str, T.Any]) -> DbBaseModel:
        obj = self.model(**data)
        db.session.add(obj)
        db.session.commit()
        return obj

    @staticmethod
    def update(obj: DbBaseModel,
               data: T.Dict[str, T.Any]) -> DbBaseModel:
        for attribute, value in data.items():
            if hasattr(obj, attribute):
                setattr(obj, attribute, value)
        db.session.commit()
        return obj

    @staticmethod
    def delete(obj: DbBaseModel):
        db.session.delete(obj)
        db.session.commit()
