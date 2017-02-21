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

    {{ dropzone.include_dropzone() }}

Step 3: Creating a form element with the class `dropzone` and id `myDropzone` in the place where you want to upload file::

    <form action="{{ url_for('upload_file') }}" class="dropzone" id="myDropzone" method="POST" enctype="multipart/form-data">
    </form>

Also to edit the action to your upload address.

More Detail
-----------

Go to `Github page
<https://github.com/greyli/flask-dropzone>`_ , which you can check for more
details.
