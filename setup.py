from setuptools import find_packages
from setuptools import setup
from glob import glob


with open("README.md","r") as fh:
    long_description = fh.read()

setup(
    name='sida',
    version='0.1.0',
    description='My first pip package',
    py_modules=[splitext(basename(path))[0] for path in glob('src/*.py')],
    # scripts=["bin/sida"],
    packages=find_packages('src'),
    package_dir={'':'src'},
    install_requires=[
        'numpy',
        'matplotlib',
        'websocket-client'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    url="https://github.com/liusida/sida",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Sida Liu",
    author_email="learner.sida.liu@gmail.com",
)