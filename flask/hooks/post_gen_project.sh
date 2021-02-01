#!/bin/bash

git_init() {
    local GIT_URL=$1
    git init
    git remote add origin $GIT_URL
    git add .
    git commit -m "Initial"
}


run_test_and_check_lint() {
    python -mvenv venv && source venv/bin/activate
    make test
    make lint
}

{% if cookiecutter.git_provider in ["bitbucket.org"] %}
    GIT_URL=https://{{cookiecutter.repo_user}}@{{cookiecutter.git_provider}}/{{cookiecutter.repo_user}}/{{cookiecutter.repo_name}}.git
{% else %}
    GIT_URL=https://{{cookiecutter.git_provider}}/{{cookiecutter.repo_user}}/{{cookiecutter.repo_name}}
{% endif %}

source ../../hooks/post_gen_project.sh

git_init $GIT_URL

run_test_and_check_lint
