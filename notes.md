# Notes

Talk Notes from https://www.youtube.com/watch?v=QgZ7qv4Cd0Y
How To Publish A Package On PyPI
by Mark Smith

0. Create a new project in github, clone it to local

1. src/, put all your source files in there

2. setup.py

3. pipenv

```bash
$pipenv install -e . #install package
$pipenv install --dev "pytest>=3.7" #for test
$pipenv shell #start shell
```

It will create Pipfile.

4. pytest

Create a folder called test, put all your test files in there.

```bash
$pytest
```

5. Manifest

Push all change to github, using following tool to create MANIFEST.in

```bash
$pip install check-manifest
$check-manifest --create
```

6. Build dist

```bash
$python setup.py bdist_wheel sdist
```

7. Twine

Upload to PyPI using following tool

```bash
$pipenv install --dev twine #install twine to dev virtual env
$pipenv shell
$twine upload dist/*
```

Username and password of PyPI are needed.

Your pip package is on air now!

8. tox

Create tox.ini, do testing in variable Python version.

```bash
tox
```

9. automatic testing using travis

Create .travis.yml file and push to github, travis will do testing for you.

and you will have an icon: ![travis auto testing](https://travis-ci.org/liusida/sida.svg?branch=master)


==================================================================

Or, you can simply use Cookiecutter

https://cookiecutter.readthedocs.io/en/latest/

```bash
$pip install cookiecutter
$cookiecutter gh:ionelmc/cookiecutter-pylibrary
```

Answer 100 questions, and done.
