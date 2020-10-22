|GithubCI| |codecov|

{{cookiecutter.repo_name}}
==================

FastAPI boilerplate

Dependencies
~~~~~~~~~~~~

Project base on `FastAPI <https://fastapi.tiangolo.com/>`__ framework -
asynchronous web framework Using
`asyncpg <https://www.sqlalchemy.org/>`__ as database library

Install and Start
~~~~~~~~~~~~~~~~~

::

    $ virtualenv venv
    $ source venv/bin/activate
    $ make dev

.. |GithubCI| image:: https://github.com/{{cookiecutter.repo_user}}/{{cookiecutter.repo_name}}/workflows/Test/badge.svg
   :target: https://github.com/{{cookiecutter.repo_user}}/{{cookiecutter.repo_name}}/actions?query=workflow%3ACI
.. |codecov| image:: https://codecov.io/gh/{{cookiecutter.repo_user}}/{{cookiecutter.repo_name}}/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/{{cookiecutter.repo_user}}/{{cookiecutter.repo_name}}
