import io
from setuptools import setup

with io.open("README.rst", "rt", encoding="utf8") as f:
    long_description = f.read()


setup(
    name='Flask-Dropzone',
    version='2.0.0',
    url='https://github.com/helloflask/flask-dropzone',
    license='MIT',
    author='Grey Li',
    author_email='withlihui@gmail.com',
    description='Upload files in Flask with Dropzone.js.',
    long_description=long_description,
    packages=['flask_dropzone'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'Flask'
    ],
    keywords='flask extension development upload',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ]
)
