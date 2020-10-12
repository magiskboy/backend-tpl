|GithubCI| |codecov|

{{cookiecutter.repo_name}}
==================

{{cookiecutter.description}}

Dependencies
~~~~~~~~~~~~

Project base on `Flask <https://flask.palletsprojects.com>`__ framework -
A micro webframework Using
`SQLAlchemy <https://www.sqlalchemy.org/>`__ as ORMs framework

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
