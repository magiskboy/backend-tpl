#!/bin/bash

source ../../hooks/post_gen_project.sh

git_init

if [[ ! -z $CI ]]; then
    run_test_and_check_lint
fi
