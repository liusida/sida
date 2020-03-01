#!/bin/sh
rm dist/*
python setup.py bdist_wheel sdist
twine upload dist/*

#w#