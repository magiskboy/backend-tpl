# coding=utf-8
import abc
from typing import (
    Dict,
    List,
    Union,
    Any,
    Optional,
    Type,
)
from types import TracebackType
from contextlib import AbstractAsyncContextManager
from asyncpg import (       #type:ignore
    Connection,
    create_pool,
)
from asyncpg.transaction import Transaction     #type:ignore


class ABCRepository(AbstractAsyncContextManager):
    __metaclass__ = abc.ABCMeta

    def __init__(
        self,
        connection: Connection
    ):
        self._in_ctx = False
        self._connection = connection
        self._current_transaction: Transaction = None

    @property
    def connection(self) -> Connection:
        return self._connection

    async def __aenter__(self):
        self._in_ctx = True
        self._current_transaction = self._connection.transaction()
        await self._current_transaction.start()
        return self

    async def __aexit__(
        self,
        exec_type: Optional[Type[BaseException]],
        exc: Optional[BaseException],
        tb: Optional[TracebackType]      #type:ignore
    ):
        self._in_ctx = False

        if exc:
            await self._current_transaction.commit()
        else:
            await self._current_transaction.rollback()
