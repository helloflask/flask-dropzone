# -*- coding: utf-8 -*-
from flask import Blueprint, current_app, url_for, Markup

#: defined normal file type
allowed_file_type = {
        'default': 'image/*, audio/*, video/*, text/*, application/*',
        'image': 'image/*',
        'audio': 'audio/*',
        'video': 'video/*',
        'text': 'text/*',
        'app': 'application/*'
    }


class _Dropzone(object):

    @staticmethod
    def load(version='5.1.1'):
        """Load Dropzone resources with given version and init dropzone configuration.

        :param version: The version of Dropzone.js.
        """
        js_filename = 'dropzone.min.js'
        css_filename = 'dropzone.min.css'

        upload_multiple = current_app.config['DROPZONE_UPLOAD_MULTIPLE']
        parallel_uploads = current_app.config['DROPZONE_PARALLEL_UPLOADS']

        if upload_multiple in [True, 'true', 'True', 1]:
            upload_multiple = 'true'

        serve_local = current_app.config['DROPZONE_SERVE_LOCAL']
        size = current_app.config['DROPZONE_MAX_FILE_SIZE']
        param = current_app.config['DROPZONE_INPUT_NAME']
        redirect_view = current_app.config['DROPZONE_REDIRECT_VIEW']

        if redirect_view is not None:
            redirect_js = '''
    this.on("queuecomplete", function(file) { 
    // Called when all files in the queue finish uploading.
    window.location = "%s";
    });''' % url_for(redirect_view)
        else:
            redirect_js = ''

        if not current_app.config['DROPZONE_ALLOWED_FILE_CUSTOM']:
            allowed_type = allowed_file_type[
                current_app.config['DROPZONE_ALLOWED_FILE_TYPE']]
        else:
            allowed_type = current_app.config['DROPZONE_ALLOWED_FILE_TYPE']

        max_files = current_app.config['DROPZONE_MAX_FILES']
        default_message = current_app.config['DROPZONE_DEFAULT_MESSAGE']
        invalid_file_type = current_app.config['DROPZONE_INVALID_FILE_TYPE']
        file_too_big = current_app.config['DROPZONE_FILE_TOO_BIG']
        server_error = current_app.config['DROPZONE_SERVER_ERROR']
        browser_unsupported = current_app.config['DROPZONE_BROWSER_UNSUPPORTED']
        max_files_exceeded = current_app.config['DROPZONE_MAX_FILE_EXCEED']

        if serve_local:
            js = '<script src="%s"></script>\n' % url_for('static', filename=js_filename)
            css = '<link rel="stylesheet" href="%s" type="text/css">\n' %\
                  url_for('static', filename=css_filename)
        else:
            js = '<script src="//cdn.bootcss.com/dropzone/%s/min/%s">' \
                 '</script>\n' % (version, js_filename)
            css = '<link rel="stylesheet" href="//cdn.bootcss.com/dropzone/%s/min/%s"' \
                  ' type="text/css">\n' % (version, css_filename)
        return Markup('''
  %s%s<script>
// var cleanFilename = function (name) {
//    return name.toLowerCase().replace(/[^\w]/gi, '');
// };
Dropzone.options.myDropzone = {
  init: function() {%s},
  uploadMultiple: %s,
  parallelUploads: %d,
  paramName: "%s", // The name that will be used to transfer the file
  maxFilesize: %d, // MB
  acceptedFiles: "%s",
  maxFiles: %s,
  dictDefaultMessage: "%s", // message display on drop area
  dictFallbackMessage: "%s",
  dictInvalidFileType: "%s",
  dictFileTooBig: "%s",
  dictResponseError: "%s",
  dictMaxFilesExceeded: "%s",
  // renameFilename: cleanFilename,
};
        </script>
        ''' % (css, js, redirect_js, upload_multiple, parallel_uploads, param, size, allowed_type, max_files,
               default_message, browser_unsupported, invalid_file_type, file_too_big,
               server_error, max_files_exceeded))

    @staticmethod
    def create(action_view='', **kwargs):
        """Create a Dropzone form with given action.

        :param action_view: The view which handle the post data.
        """
        return Markup('''<form action="%s" method="post" class="dropzone" id="myDropzone" 
        enctype="multipart/form-data"></form>''' % url_for(action_view, **kwargs))

    @staticmethod
    def style(css):
        """Add css to dropzone.

        :param css: style sheet code.
        """
        return Markup('<style>\n.dropzone{%s}\n</style>'% css)


class Dropzone(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):

        blueprint = Blueprint('dropzone', __name__)
        app.register_blueprint(blueprint)

        if not hasattr(app, 'extensions'):
            app.extesions = {}
        app.extensions['dropzone'] = _Dropzone
        app.context_processor(self.context_processor)

        # settings
        app.config.setdefault('DROPZONE_SERVE_LOCAL', False)
        app.config.setdefault('DROPZONE_MAX_FILE_SIZE', 3)  # MB
        app.config.setdefault('DROPZONE_INPUT_NAME', 'file')
        app.config.setdefault('DROPZONE_ALLOWED_FILE_CUSTOM', False)
        app.config.setdefault('DROPZONE_ALLOWED_FILE_TYPE', 'default')
        app.config.setdefault('DROPZONE_MAX_FILES', 'null')
        
        # The view to redierct when upload was completed.
        app.config.setdefault('DROPZONE_REDIRECT_VIEW', None)
        
        # Whether to send multiple files in one request.
        # In default, each file will send with a request.
        # Then you can use ``request.files.getlist('paramName')`` to 
        # get a list of uploads.
        app.config.setdefault('DROPZONE_UPLOAD_MULTIPLE', 'false')
        
        # When ``DROPZONE_UPLOAD_MULTIPLE`` set to True, this will
        # defined how many uploads will handled in per request.
        app.config.setdefault('DROPZONE_PARALLEL_UPLOADS', 2)

        # messages
        app.config.setdefault('DROPZONE_DEFAULT_MESSAGE', "Drop files here to upload")
        app.config.setdefault('DROPZONE_INVALID_FILE_TYPE', "You can't upload files of this type.")
        app.config.setdefault('DROPZONE_FILE_TOO_BIG',
                              "File is too big {{filesize}}. Max filesize: {{maxFilesize}}MiB.")
        app.config.setdefault('DROPZONE_SERVER_ERROR', "Server error: {{statusCode}}")
        app.config.setdefault('DROPZONE_BROWSER_UNSUPPORTED',
                              "Your browser does not support drag'n'drop file uploads.")
        app.config.setdefault('DROPZONE_MAX_FILE_EXCEED', "Your can't upload any more files.")

    @staticmethod
    def context_processor():
        return {
            'dropzone': current_app.extensions['dropzone']
        }
