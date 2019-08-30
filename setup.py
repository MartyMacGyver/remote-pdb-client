#!/usr/bin/env python3

from os import path
from setuptools import setup


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

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

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
