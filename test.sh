#!/bin/sh
coverage run test.py
coverage report -m
coverage html

python -m unittest test
