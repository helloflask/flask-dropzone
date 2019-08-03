===============
Flask-Dropzone
===============

Flask-Dropzone packages `Dropzone.js
<http://dropzonejs.com>`_ into an extension to add file upload support for Flask.
It can create links to serve Dropzone from a CDN and works with no JavaScript code in your application.

NOTICE: This extension is built for simple usage, if you need more flexibility, please use Dropzone.js directly.

Basic Usage
-----------

Step 1: Initialize the extension:

.. code-block:: python

    from flask_dropzone import Dropzone

    dropzone = Dropzone(app)


Step 2: In your `<head>` section of your base template add the following code::

    <head>
    {{ dropzone.load_css() }}
    </head>
    <body>
    ...
    {{ dropzone.load_js() }}
    </body>

You can assign the version of Dropzone.js through `version` argument, the default value is `5.2.0`.
Step 3: Creating a Drop Zone with `create()`, and configure it with `config()`::

    {{ dropzone.create(action='the_url_which_handle_uploads') }}
    ...
    {{ dropzone.config() }}

Also to edit the action view to yours.

Beautify Dropzone
-----------------

Style it according to your preferences through `style()` method::

    {{ dropzone.style('border: 2px dashed #0087F7; margin: 10%; min-height: 400px;') }}

More Detail
-----------

Go to `Documentation
<https://flask-dropzone.readthedocs.io/en/latest/>`_ , which you can check for more
details.
