#!/bin/bash

git_init() {
    git init
    git remote add-url origin https://{{cookiecutter.git_provider}}/{{cookiecutter.repo_user}}/{{cookiecutter.repo_name}}
    git add .
    git commit -m "Initial"
}


run_test_and_check_lint() {
    python -mvenv venv && source venv/bin/activate
    make test
    make lint
}

