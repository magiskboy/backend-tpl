#!/bin/bash

{% if cookiecutter.git_provider in ["bitbucket.org"] %}
    GIT_URL=https://{{cookiecutter.repo_user}}@{{cookiecutter.git_provider}}/{{cookiecutter.repo_user}}/{{cookiecutter.repo_name}}.git
{% else %}
    GIT_URL=https://{{cookiecutter.git_provider}}/{{cookiecutter.repo_user}}/{{cookiecutter.repo_name}}
{% endif %}

source ../../hooks/post_gen_project.sh

git_init $GIT_URL

if [[ ! -z $CI ]]; then
    run_test_and_check_lint
fi
