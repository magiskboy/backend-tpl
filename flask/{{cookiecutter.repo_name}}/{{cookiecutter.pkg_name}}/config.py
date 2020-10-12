#coding=utf-8

import os


class Config:
    HOST = os.getenv('HOST', '0.0.0.0')

    PORT = int(os.getenv('PORT', '5000'))

    SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI', 'sqlite:///:memory:')

    SQLALCHEMY_TRACK_MODIFICATIONS = True

    TESTING = False

    DEBUG = False


class DevelopmentConfig(Config):
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'sqlite:///dev.db'


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    pass


def get_config(config_name):
    return {
        'development': DevelopmentConfig,
        'testing': TestingConfig,
        'production': ProductionConfig,
    }.get(config_name)
