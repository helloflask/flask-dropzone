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
(recommended), you can also use this methods to load resources:

.. code-block:: jinja

    <head>
    {{ dropzone.load_css() }}
    </head>
    <body>
    ...
    {{ dropzone.load_js() }}
    </body>

.. tip::
    There is a ``dropzone.load()`` method that was a combination of
    ``dropzone.load_css()`` and ``dropzone.load_js()``, but we recommend not
    to use this method for page load performance consideration. Also,
    ``dropzone.load()`` will be removed in the near future.

You can assign the version of Dropzone.js through ``version`` argument,
the default value is ``5.2.0``. And, you can pass ``css_url`` and
``js_url`` separately to customize resources URL.

Create a Drop Zone
-------------------

Creating a Drop Zone with ``create()`` and use ``config()``
to make the configuration come into effect:

.. code-block:: jinja

    {{ dropzone.create(action='the_url_or_endpoint_which_handle_uploads') }}
    ...
    {{ dropzone.config() }}
    </body>

Remember to edit the ``action`` to the URL or endpoint which handles the
uploads, for example ``dropzone.create(action='upload_view')`` or
``dropzone.create(action=url_for('upload_view')')``.

Beautify Dropzone
-----------------

Style it according to your preferences through ``dropzone.style()`` method:

.. code-block:: jinja

    <head>
    {{ dropzone.load_css() }}
    {{ dropzone.style('border: 2px dashed #0087F7; margin: 10%; min-height: 400px;') }}
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

