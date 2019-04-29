#!/usr/bin/env python3

"""
    Copyright (c) 2017 Martin F. Falatic

    Permission is hereby granted, free of charge, to any person obtaining a copy
    of this software and associated documentation files (the "Software"), to deal
    in the Software without restriction, including without limitation the rights
    to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
    copies of the Software, and to permit persons to whom the Software is
    furnished to do so, subject to the following conditions:

    The above copyright notice and this permission notice shall be included in
    all copies or substantial portions of the Software.

    THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
    IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
    FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
    AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
    LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
    OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
    THE SOFTWARE.
"""

from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


def read_and_exec_conf(conf_file):
    conf = {}
    exec_str = ''
    with open(conf_file, 'r', encoding='utf-8') as f:
        for line in f:
            exec_str += line.rstrip('\r\n') + '\n'
        exec_str = exec_str.lstrip(u'\ufeff')
        exec(exec_str, conf)
    return conf


config = read_and_exec_conf('remotepdb_client/__config__.py')
package_data = config['PACKAGE_DATA']

setup(
    name=package_data['name'],
    version=package_data['version'],
    description=package_data['description'],
    url=package_data['url'],
    author=package_data['author'],
    author_email=package_data['author_email'],
    license=package_data['license'],
    classifiers=package_data['classifiers'],
    keywords=package_data['keywords'],
    packages=package_data['packages'],
    entry_points=package_data['entry_points'],
    install_requires=package_data['install_requires'],
    extras_require=package_data['extras_require'],
    package_data=package_data['package_data'],
    data_files=package_data['data_files'],
    # Derived data
    long_description=long_description,
    long_description_content_type='text/markdown',
)
