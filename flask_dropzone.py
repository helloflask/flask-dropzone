# -*- coding: utf-8 -*-
from jinja2 import Markup
from flask import current_app


#: defined normal file type
allowed_file_type = {
        'default': 'image/*, audio/*, video/*, text/*, application/*',
        'image': 'image/*',
        'audio': 'audio/*',
        'video': 'video/*',
        'text': 'text/*',
        'app': 'application/*'
    }


class _dropzone(object):

    @staticmethod
    def include_dropzone(version='4.3.0'):
        js = ''
        css = ''
        serve_local = current_app.config['DROPZONE_SERVE_LOCAL']
        size = current_app.config['DROPZONE_MAX_FILE_SIZE']
        param = current_app.config['DROPZONE_INPUT_NAME']

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
        if serve_local == True:
            js = '''<script src="{{ url_for('static', filename='dropzone.js') }}"></script>\n'''
            css = '''<link rel="stylesheet" href="{{ url_for('static', filename='dropzone.css') }}"
                type="text/css">\n'''
        elif version is not None:
            js_filename = 'dropzone.js'
            css_filename = 'dropzone.css'
            js = '<script src="//cdn.bootcss.com/dropzone/%s/%s">' \
                '</script>\n' % (version, js_filename)
            css = '<link rel="stylesheet" href="//cdn.bootcss.com/dropzone/%s/%s"' \
                  ' type="text/css">\n' % (version, css_filename)
        return Markup('''%s%s<script>
var cleanFilename = function (name) {
   return name.toLowerCase().replace(/[^\w]/gi, '');
};
Dropzone.options.myDropzone = {
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
        ''' % (css, js, param, size, allowed_type, max_files,
               default_message, invalid_file_type, file_too_big,
               server_error, browser_unsupported, max_files_exceeded))


class Dropzone(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        if not hasattr(app, 'extensions'):
            app.extesions = {}
        app.extensions['dropzone'] = _dropzone
        app.context_processor(self.context_processor)

        # setting
        app.config.setdefault('DROPZONE_SERVE_LOCAL', False)
        app.config.setdefault('DROPZONE_MAX_FILE_SIZE', 3)  # MB
        app.config.setdefault('DROPZONE_INPUT_NAME', 'file')
        app.config.setdefault('DROPZONE_ALLOWED_FILE_CUSTOM', False)
        app.config.setdefault('DROPZONE_ALLOWED_FILE_TYPE', allowed_file_type['default'])
        app.config.setdefault('DROPZONE_MAX_FILES', 'null')

        # messages
        app.config.setdefault('DROPZONE_DEFAULT_MESSAGE', "Drop files here to upload")
        app.config.setdefault('DROPZONE_INVALID_FILE_TYPE', "You can't upload files of this type.")
        app.config.setdefault('DROPZONE_FILE_TOO_BIG', "File is too big {{filesize}}. Max filesize: {{maxFilesize}}MiB.")
        app.config.setdefault('DROPZONE_SERVER_ERROR', "Server error: {{statusCode}}")
        app.config.setdefault('DROPZONE_BROWSER_UNSUPPORTED', "Your browser does not support drag'n'drop file uploads.")
        app.config.setdefault('DROPZONE_MAX_FILE_EXCEED', "Your can't upload any more files.")

    @staticmethod
    def context_processor():
        return {
            'dropzone': current_app.extensions['dropzone']
        }

