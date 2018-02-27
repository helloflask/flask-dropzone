# -*- coding: utf-8 -*-
"""
    Flask-Dropzone
    --------------
    :copyright: (c) 2017 by Grey Li.
    :license: MIT, see LICENSE for more details.
    Upload file in Flask with Dropzone.js.
"""
from setuptools import setup

with open('README.rst') as f:
    long_description = f.read()


setup(
    name='Flask-Dropzone',
    version='1.4.2',
    url='https://github.com/greyli/flask-dropzone',
    download_url='https://github.com/greyli/flask-dropzone/tarball/1.4.1',
    license='MIT',
    author='Grey Li',
    author_email='withlihui@gmail.com',
    description='Upload file in Flask with Dropzone.js.',
    long_description=long_description,
    py_modules=['flask_dropzone'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    keywords='flask extension development upload',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
