# Notes

Talk Notes from https://www.youtube.com/watch?v=QgZ7qv4Cd0Y
How To Publish A Package On PyPI
by Mark Smith

## Github

Create a new project in github, clone it to local

## Source files

Create a folder 'src/', put all your source files in there

## setup.py

## pipenv

```bash
$pipenv install -e . #install package
$pipenv install --dev "pytest>=3.7" #for test
$pipenv shell #start shell
```

It will create Pipfile. (Notice: using `pipenv shell`, and then `pip install package-name` can not let pipenv know the dependencies. Only use pipenv install to install any package. Or, never use `pipenv shell`.)

## pytest

Create a folder called test, put all your test files in there.

```bash
$pytest
```

## Manifest

Push all change to github, using following tool to create MANIFEST.in

```bash
$pip install check-manifest
$check-manifest --create
```

## Build dist

```bash
$python setup.py bdist_wheel sdist
```

## Twine

Upload to PyPI using following tool

```bash
$pipenv install --dev twine #install twine to dev virtual env
$pipenv shell
$twine upload dist/*
```

Username and password of PyPI are needed.

or just use any twine to upload it. And before uploading, delete other files in dist/*, otherwise you will get a FileAlreadyExist error from PyPI.

```bash
$pip install twine
$twine upload dist/*
```

Your pip package is on air now!

## tox

Create tox.ini, do testing in variable Python version.

```bash
tox
```

## automatic testing using travis

Create .travis.yml file and push to github, travis will do testing for you.

and you will have an icon: ![travis auto testing](https://travis-ci.org/liusida/sida.svg?branch=master)


==================================================================

## Automatic

Or, you can simply use Cookiecutter

https://cookiecutter.readthedocs.io/en/latest/

```bash
$pip install cookiecutter
$cookiecutter gh:ionelmc/cookiecutter-pylibrary
```

Answer 100 questions, and done.

==================================================================

Furthermore,

## Scripts, Executable

If you want to put an executable file in your package, you can create a folder like 'bin/', and in setup.py, add:

```python
    scripts=["bin/sida"],
```

## Dependencies

If your program is depend on other packages, like 'numpy', in setup.py, add:

```python
    install_requires=[
        'numpy',
    ],
```
