Flask-Dropzone
================
Upload file in Flask with [Dropzone.js](http://www.dropzonejs.com/).

Installation
------------
    pip install flask-dropzone


Quick Start
-----------

Step 1: Initialize the extension:

    from flask_dropzone import Dropzone
    
    dropzone = Dropzone(app)

This extension also supports the [Flask application factory pattern](http://flask.pocoo.org/docs/latest/patterns/appfactories/) by allowing you to create a Dropzone object and then separately initialize it for an app:

        dropzone = Dropzone()

        def create_app(config):
            app = Flask(__name__)
            app.config.from_object(config)
            
            dropzone.init_app(app)
            ...
            
            return app

Step 2: In your `<head>` section of your template add the following code:
    
    {{ dropzone.include_dropzone() }}

Step 3: Creating a form element with the class `dropzone` and id `myDropzone` in the place where you want to upload file:
 
    <form action="{{ url_for('upload_file') }}" class="dropzone" id="myDropzone" method="POST" enctype="multipart/form-data">
    </form>

Also to edit the action to your upload address.

Configuration 
-------------

The supported list of config options is shown below:

| Name                     | Default Value | Info |
| ------------------------ | ------------- | ---- |
| `DROPZONE_SERVE_LOCAL`   | False         | default to use CDN |
| `DROPZONE_MAX_FILE_SIZE` | 3             | unit: MB   |
| `DROPZONE_INPUT_NAME`    | `file`        | `<input type="file" name="file">` |
| `DROPZONE_ALLOWED_FILE_CUSTOM` | False | see detail below |
| `DROPZONE_ALLOWED_FILE_TYPE` | `allowed_file_type['default']` | see detail below |
| `DROPZONE_MAX_FILES` | 'null' | the max files user can upload once |
| `DROPZONE_DEFAULT_MESSAGE` | "Drop files here to upload" | message displayed on drop area |
| `DROPZONE_INVALID_FILE_TYPE` |  "You can't upload files of this type." | error message |
| `DROPZONE_FILE_TOO_BIG` | "File is too big {{filesize}}. Max filesize: {{maxFilesize}}MiB." | error message |
| `DROPZONE_SERVER_ERROR` | "Server error: {{statusCode}}" |  error message |
| `DROPZONE_BROWSER_UNSUPPORTED` | "Your browser does not support drag'n'drop file uploads." | error message | 
| `DROPZONE_MAX_FILE_EXCEED` | "Your can't upload any more files." |  error message |


You can use these file type: 
    
    allowed_file_type = {
            'default': 'image/*, audio/*, video/*, text/*, application/*',
            'image': 'image/*',
            'audio': 'audio/*',
            'video': 'video/*',
            'text': 'text/*',
            'app': 'application/*'
        }
        
If you want to set the allowed file type by yourself, you need to set 
`DROPZONE_ALLOWED_FILE_CUSTOM` to `True`, then add mime type or file extensions to
`DROPZONE_ALLOWED_FILE_TYPE`, such as:

    app.config[`DROPZONE_ALLOWED_FILE_TYPE`] = 'image/*, .pdf, .txt'

Consult the [dropzone.js documentation](http://dropzonejs.com/) for details on these options.

Beautify Dropzone
==================

Just add a border and background:

    .dropzone {
        border: 2px dashed #0087F7;
        background: #ddd;
    }

ChangeLog
=========
1.3
---
* Documentation fix.

1.2
---
* Upload address fix.
* Delete useless code.

1.1
----
* Add more configuration options.
* Support local resource serve.
* Add basic documentation.

1.0
----
* Init release.
