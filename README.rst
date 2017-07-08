===============
Flask-Dropzone
===============

Flask-Dropzone packages `Dropzone.js
<http://dropzonejs.com>`_ into an extension to add file upload support for Flask.
It can create links to serve Dropzone from a CDN and works with no JavaScript code in your application.

Basic Usage
-----------

Step 1: Initialize the extension::

    from flask_dropzone import Dropzone

    dropzone = Dropzone(app)


Step 2: In your `<head>` section of your base template add the following code::

    {{ dropzone.load() }}

You can assign the version of Dropzone.js through `version` argument, the default value is `5.1.1`.
Step 3: Creating a Drop Zone with `create()`:

    {{ dropzone.create(action_view='upload_view') }}

Also to edit the action view to yours.

Beautify Dropzone
-----------------

Style it according to your preferences through `style()` method:

    {{ dropzone.style('border: 2px dashed #0087F7; margin: 10%; min-height: 400px;') }}

More Detail
-----------

Go to `Github page
<https://github.com/greyli/flask-dropzone>`_ , which you can check for more
details.
