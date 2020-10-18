# coding=utf-8

import os
import click
import uvicorn      #type:ignore
from {{cookiecutter.pkg_name}} import api


app = api.create_asgi()


@click.group()
def cli():
    pass


@cli.command()
def dev():
    """Run application in development
    In this environment, app working on the process and
    it auto reload when code updated
    """
    global app      #pylint:disable=W0603,C0103

    if not workers:
        workers = os.cpu_count()
    uvicorn.run('{{cookiecutter.pkg_name}}.__main__:app',
                host='127.0.0.1',
                port=8000,
                reload=True,
                workers=1,
                log_level='debug',
                loop='uvloop')


@cli.command()
def routes():
    """List all of routes in application
    """
    global app      #pylint:disable=W0603,C0103

    data = []
    for route in app.routes:        #pylint:disable=E1101
        data.append([route.name, ', '.join(route.methods), route.path])

    # print header line
    print(f'{"Name":<30} {"Methods":<30} {"Path":<60}')
    print('-'*90)

    # print content lines
    for name, methods, path in data:
        print(f'{name:<30} {methods:<30} {path:<60}')


if __name__ == '__main__':
    cli()
