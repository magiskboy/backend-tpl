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

