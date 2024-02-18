Basic Usage
=============

Installation
------------

.. code-block:: bash

    $ pip install flask-dropzone

Initialization
---------------

Initialize the extension:

.. code-block:: python

    from flask_dropzone import Dropzone

    app = Flask(__name__)
    dropzone = Dropzone(app)

This extension also supports the `Flask application factory
pattern <http://flask.pocoo.org/docs/latest/patterns/appfactories/>`__
by allowing you to create a Dropzone object and then separately
initialize it for an app:

.. code-block:: python

    dropzone = Dropzone()

    def create_app(config):
        app = Flask(__name__)
        ...
        dropzone.init_app(app)
        ...
        return app

Include Dropzone.js Resources
-------------------------------

In addition to manage and load resources by yourself
(recommended), you can also use these methods to load resources:

.. code-block:: jinja

    <head>
    {{ dropzone.load_css() }}
    </head>
    <body>
    ...
    {{ dropzone.load_js() }}
    </body>

You can assign the version of Dropzone.js through ``version`` argument,
the default value is ``5.2.0``. And, you can pass ``css_url`` and
``js_url`` separately to customize resources URL.

Create a Drop Zone
-------------------

Creating a Drop Zone with ``create()`` and use ``config()``
to make the configuration come into effect:

.. code-block:: jinja

    <body>
    {{ dropzone.create(action='the_url_or_endpoint_which_handle_uploads') }}
    ...
    {{ dropzone.config() }}
    </body>

Remember to edit the ``action`` to the URL or endpoint which handles the
uploads, for example ``dropzone.create(action='upload_view')`` or
``dropzone.create(action=url_for('upload_view'))``.

The default ID of the dropzone form element is `myDropzone`, usually you don't
need to change it. If you have specific need, for example, you want to have multiple
dropzones on one page, you can use the ``id`` parameter to assign the id:

.. code-block:: jinja
    
    <body>
    {{ dropzone.create(id='foo') }}
    {{ dropzone.create(id='bar') }}
    ...
    {{ dropzone.config(id='foo') }}
    {{ dropzone.config(id='bar') }}
    </body>

Notice that the same id must passed both in ``dropzone.create()`` and ``dropzone.config()``.

Beautify Dropzone
-----------------

Style it according to your preferences through ``dropzone.style()`` method:

.. code-block:: jinja

    <head>
    {{ dropzone.load_css() }}
    {{ dropzone.style('border: 2px dashed #0087F7; margin: 10%; min-height: 400px;') }}
    </head>

Notice that you could use manual ``<style>`` entry for more flexibility:

.. code-block:: jinja

    <head>
    {{ dropzone.load_css() }}
    <style>
        .dropzone {
            border: 2px dashed #0087F7;
            margin: 10%;
            min-height: 400px;
        }
    </style>
    </head>

This would apply CSS code to all the dropzones on the page. If you have specific need, for example,
you want to have unique styles for multiple dropzones on one page, you can use the ``id`` parameter to
assign the id:

.. code-block:: jinja

    <head>
    {{ dropzone.load_css() }}
    {{ dropzone.style('border: 2px dashed #0087F7; margin: 10%; min-height: 400px;', id='foo') }}
    {{ dropzone.style('border: 4px dashed #0087F7; margin: 20%; min-height: 600px;', id='bar') }}
    </head>

Save Uploads with Flask
-----------------------

When the file was dropped on drop zone, you can get the uploaded file
in ``request.files``, just pass upload input's name attribute (default to ``file``).

.. code-block:: python

    import os

    from flask import Flask, request
    from flask_dropzone import Dropzone

    app = Flask(__name__)

    dropzone = Dropzone(app)

    @app.route('/uploads', methods=['GET', 'POST'])
    def upload():

        if request.method == 'POST':
            f = request.files.get('file')
            f.save(os.path.join('the/path/to/save', f.filename))

        return 'upload template'


.. tip:: See ``examples/basic`` for more detail.

