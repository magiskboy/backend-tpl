#!/bin/sh

. ../hooks/post_gen_project.sh

git_init

run_test_and_check_lint
