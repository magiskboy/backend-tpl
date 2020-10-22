# coding=utf-8

import fastapi
from starlette.middleware.cors import CORSMiddleware
from {{cookiecutter.pkg_name}}.core.database import (
    get_db,
    db_pool,
    setup_database,
)
from {{cookiecutter.pkg_name}}.core.web import FastAPISetting
from {{cookiecutter.pkg_name}}.api import v1


def create_asgi() -> fastapi.FastAPI:
    """Function facetory for create a new ASGI object"""
    setting = FastAPISetting()
    app = fastapi.FastAPI(
        title=setting.SERVICE_NAME,
        debug=setting.DEBUG,
    )
    app.add_middleware(
        CORSMiddleware,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    @app.get('/health')
    async def health():         #pylint:disable=W0612
        return fastapi.Response('', 204)

    app.include_router(v1.api_router, prefix='/v1')

    @app.on_event('startup')
    async def startup_event():      #pylint:disable=W0612
        await setup_database()    # create the pool connection

    @app.on_event('shutdown')
    async def shutdown_event():     #pylint:disable=W0612
        await db_pool.close()   # attemp close all connections

    return app
