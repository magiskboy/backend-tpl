# coding=utf-8
from typing import Optional
from pydantic import BaseSettings


class FastAPISetting(BaseSettings):
    SERVICE_NAME: str = '{{cookiecutter.pkg_name}}'

    DEBUG: bool = False

    SENTRY_DSN: Optional[str] = None

    class Config:
        case_sensitive=False
