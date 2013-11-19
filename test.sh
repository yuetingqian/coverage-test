#!/bin/sh
set -e
coverage run test.py
coverage report -m
coverage html

python -m unittest test

ls -l  htmlcov/
