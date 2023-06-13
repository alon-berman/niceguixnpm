# nicegui x npm

This is a lovely demo that allowing you to use external npm 
packages in your .js files.
In this example, the leaderline component is a custom vue component
which is based on the [leader-line](https://www.npmjs.com/package/leader-line) package.


## The trick
We install locally the npm packages, and then copy the entire folder to an accessible path using
nicegui's `add_static_files()` method.


## Prerequisites
* [npm](https://npmjs.com)
* [Python 3.8.11](https://www.python.org/downloads/release/python-3811/)

## Set Up Installation

    $ npm install
    $ pip install requirements.txt
    

## Quickstart


    $ python main.py
