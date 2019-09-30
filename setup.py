from setuptools import setup

with open("README.md","r") as fh:
    long_description = fh.read()

setup(
    name='sida',
    version='0.0.3',
    description='My first pip package',
    py_modules=["sida"],
    scripts=["bin/sida"],
    package_dir={'':'src'},
    install_requires=[
        'numpy',
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