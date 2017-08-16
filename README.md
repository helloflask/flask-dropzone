Flask-Dropzone
================
Upload file in Flask with [Dropzone.js](http://www.dropzonejs.com/).

[中文文档](http://greyli.com/flask-dropzone-add-file-upload-capabilities-for-your-project/)

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
    
    {{ dropzone.load() }}

You can assign the version of Dropzone.js through `version` argument, the default value is `5.1.1`.
Step 3: Creating a Drop Zone with `create()`:
 
    {{ dropzone.create(action_view='upload_view') }}

Also to edit the action view to yours.

Beautify Dropzone
-----------------

Style it according to your preferences through `style()` method:

    {{ dropzone.style('border: 2px dashed #0087F7; margin: 10%; min-height: 400px;') }}


Configuration 
-------------

The supported list of config options is shown below:

| Name                     | Default Value | Info |
| ------------------------ | ------------- | ---- |
| `DROPZONE_SERVE_LOCAL`   | False         | default to use CDN |
| `DROPZONE_MAX_FILE_SIZE` | 3             | unit: MB   |
| `DROPZONE_INPUT_NAME`    | `file`        | `<input type="file" name="file">` |
| `DROPZONE_ALLOWED_FILE_CUSTOM` | False | see detail below |
| `DROPZONE_ALLOWED_FILE_TYPE` | `'default'` | see detail below |
| `DROPZONE_MAX_FILES` | 'null' | the max files user can upload once |
| `DROPZONE_DEFAULT_MESSAGE` | "Drop files here to upload" | message displayed on drop area |
| `DROPZONE_INVALID_FILE_TYPE` |  "You can't upload files of this type." | error message |
| `DROPZONE_FILE_TOO_BIG` | "File is too big {{filesize}}. Max filesize: {{maxFilesize}}MiB." | error message |
| `DROPZONE_SERVER_ERROR` | "Server error: {{statusCode}}" | error message |
| `DROPZONE_BROWSER_UNSUPPORTED` | "Your browser does not support drag'n'drop file uploads." | error message | 
| `DROPZONE_MAX_FILE_EXCEED` | "Your can't upload any more files." | error message |
| `DROPZONE_UPLOAD_MULTIPLE` | 'false' | whether to send multiple files in one request. |
| `DROPZONE_PARALLEL_UPLOADS` | 2 | how many uploads will handled in per request when `DROPZONE_UPLOAD_MULTIPLE` set to True. |


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


Save uploads with Flask
-----------------------
    import os

    from flask import Flask, request
    from flask_dropzone import Dropzone

    app = Flask(__name__)

    dropzone = Dropzone(app)

    @app.route('/uploads', methods=['GET', 'POST'])
    def upload():

        if request.method == 'POST':
            f = request.files['input_name']
            f.save(os.path.join(the_path_to_save, f.filename))

        return 'upload template'

If you set `DROPZONE_UPLOAD_MULTIPLE` as True, then you need to save multiple uploads in per request:

    ...
    app.config['DROPZONE_UPLOAD_MULTIPLE'] = True

    @app.route('/upload', methods=['GET', 'POST'])
    def upload():

        if request.method == 'POST':
            for f in request.files.getlist('input_name'):
                f.save(os.path.join(the_path_to_save, f.filename))

        return 'upload template'


See example for more detail.


Todo
-----

* A Proper Documentation
* Test
* Auto redirect when the upload was completed (see detail on this [SO answer](https://stackoverflow.com/a/42264730/5511849)).

