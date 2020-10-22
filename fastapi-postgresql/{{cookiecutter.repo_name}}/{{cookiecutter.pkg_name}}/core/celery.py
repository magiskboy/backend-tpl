from typing import Optional
import os
import asyncio
from pydantic import BaseSettings
from celery import Celery
from celery.utils.log import get_task_logger
from celery.signals import worker_init
from {{cookiecutter.pkg_name}}.core.database import setup_database


class CeleryConfig(BaseSettings):
    broker_url: Optional[str] = 'amqp://celery:password@localhost:5672/celery'

    result_backend: Optional[str] = 'rpc://'

    result_persistent = False

    result_serializer: Optional[str] = 'msgpack'

    task_serializer: Optional[str] = 'msgpack'

    worker_concurrency: Optional[int] = os.cpu_count()

    accept_content = ['msgpack']

    class Config:
        case_sensitive = False

        fields = {
            'broker_url': {
                'env': 'CELERY_BROKER_URL',
            },
            'result_backend': {
                'env': 'CELERY_RESULT_BACKEND',
            },
            'result_serializer': {
                'env': 'CELERY_RESULT_SERIALIZER',
            },
            'task_serializer': {
                'env': 'CELERY_TASK_SERIALIZER',
            },
            'worker_concurrency': {
                'env': 'CELERY_CELERYD_CONCURRENCY',
            }
        }

app = Celery(__name__)
app.config_from_object(CeleryConfig())

logger = get_task_logger(__name__)


@worker_init.connect
def init_database_pool(**kwargs):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(setup_database())
    logger.info('Connect to database successful')
