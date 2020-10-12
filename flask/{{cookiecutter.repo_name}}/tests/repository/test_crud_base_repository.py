# coding=utf-8

import sqlalchemy as sa
from tests.repository import RepositoryTestCase
from {{cookiecutter.pkg_name}}.repository import CRUDBase
from {{cookiecutter.pkg_name}}.model import (
    db,
    Base,
)


class Item(Base):
    name = sa.Column(sa.String(20))


class ItemRepository(CRUDBase):
    pass


class CRUDBaseTestCase(RepositoryTestCase):
    __repoclass__ = ItemRepository
    __args__ = (Item,)

    def setUp(self):
        self.items = []
        for i in range(5):
            item = Item(name=f'Item {i}')
            db.session.add(item)
            self.items.append(item)
        db.session.commit()

    def test_get_item(self):
        ret = self.repo.get(self.items[0].id_)
        assert ret == self.items[0]

    def test_get_multi_item(self):
        rets = self.repo.get_multi(0, 2, False)
        assert isinstance(rets, list)
        assert 2 == len(rets)
        for i, item in enumerate(rets):
            assert i + 1 == item.id_

    def test_get_multi_item_with_lazy_load(self):
        rets = self.repo.get_multi(0, 2)
        assert isinstance(rets, sa.orm.query.Query)
        for i, item in enumerate(rets):
            assert i + 1 == item.id_

    def test_create_item(self):
        data = {'name': 'Test create item'}
        ret = self.repo.create(data)
        assert ret.id_
        assert data['name'] == ret.name

    def test_update_item(self):
        item = self.items[0]
        id_before = item.id_
        data = {'name': 'Test update item'}
        ret = self.repo.update(item, data)
        assert data['name'] == ret.name
        assert id_before == ret.id_

    def test_delete_item(self):
        item = self.items[0]
        self.repo.delete(item)
        assert None == db.session.query(Item).get(item.id_)
