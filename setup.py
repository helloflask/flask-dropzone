# -*- coding: utf-8 -*-
"""
Flask-Dropzone
--------------

Upload file in Flask with Dropzone.js.
"""
from setuptools import setup


setup(
    name='Flask-Dropzone',
    version='1.0',
    url='https://github.com/greyli/flask-dropzone',
    download_url='https://github.com/greyli/flask-dropzone/tarball/1.0',
    license='MIT',
    author='Grey Li',
    author_email='withlihui@gmail.com',
    description='Upload file in Flask with Dropzone.js.',
    long_description=__doc__,
    py_modules=['flask_dropzone'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]

)