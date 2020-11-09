from typing import Optional
from pydantic import BaseSettings
from asyncpg.pool import Pool
from asyncpg import create_pool


db_pool: Pool = None


class PostgresConfig(BaseSettings):
    dsn: Optional[str] = 'postgres://postgres:password@localhost:5432/{{pkg_name}}'

    min_size: Optional[int] = 10

    max_size: Optional[int] = 10

    class Config:
        case_sensitive=False

        fields = {
            'dsn': {
                'env': 'DATABASE_DSN'
            },
            'min_size': {
                'env': 'DATABASE_MIN_POOL_SIZE',
            },
            'max_size': {
                'env': 'DATABASE_MAX_POOL_SIZE',
            },
        }


async def setup_database():
    global db_pool      #pylint:disable=C0103
    db_pool = await create_pool(**PostgresConfig().dict())


async def get_db():
    global db_pool      #pylint:disable=C0103
    async with db_pool.acquire() as db:     #pylint:disable=C0103
        yield db
