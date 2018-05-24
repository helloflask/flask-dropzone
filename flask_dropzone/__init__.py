# -*- coding: utf-8 -*-
import os
import uuid

from flask import Blueprint, current_app, url_for, Markup, render_template_string

#: defined normal file type
allowed_file_type = {
    'default': 'image/*, audio/*, video/*, text/*, application/*',
    'image': 'image/*',
    'audio': 'audio/*',
    'video': 'video/*',
    'text': 'text/*',
    'app': 'application/*'
}


#: generate a random filename, replacement for werkzeug.secure_filename
def random_filename(old_filename):
    ext = os.path.splitext(old_filename)[1]
    new_filename = uuid.uuid4().hex + ext
    return new_filename


class _Dropzone(object):

    @staticmethod
    def load(js_url='', css_url='', version='5.2.0'):
        """Load Dropzone resources with given version and init dropzone configuration.

        .. versionchanged:: 1.4.3
        Added `js_url` and `css_url` parameters to pass custom resource URL.

        :param js_url: The JavaScript url for Dropzone.js.
        :param css_url: The CSS url for Dropzone.js.
        :param version: The version of Dropzone.js.
        """
        js_filename = 'dropzone.min.js'
        css_filename = 'dropzone.min.css'

        upload_multiple = current_app.config['DROPZONE_UPLOAD_MULTIPLE']
        parallel_uploads = current_app.config['DROPZONE_PARALLEL_UPLOADS']

        if upload_multiple in [True, 'true', 'True', 1]:
            upload_multiple = 'true'
        else:
            upload_multiple = 'false'

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
            js = '<script src="%s"></script>\n' % url_for('dropzone.static', filename=js_filename)
            css = '<link rel="stylesheet" href="%s" type="text/css">\n' % \
                  url_for('dropzone.static', filename=css_filename)
        else:
            js = '<script src="//cdn.bootcss.com/dropzone/%s/min/%s">' \
                 '</script>\n' % (version, js_filename)
            css = '<link rel="stylesheet" href="//cdn.bootcss.com/dropzone/%s/min/%s"' \
                  ' type="text/css">\n' % (version, css_filename)

        if js_url:
            js = '<script src="%s"></script>\n' % js_url
        if css_url:
            css = '<link rel="stylesheet" href="%s" type="text/css">\n' % css_url

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
    def load_css(version='5.2.0', css_url=None):
        css_filename = 'dropzone.min.css'
        serve_local = current_app.config['DROPZONE_SERVE_LOCAL']

        if serve_local:
            css = '<link rel="stylesheet" href="%s" type="text/css">\n' % \
                  url_for('dropzone.static', filename=css_filename)
        else:
            css = '<link rel="stylesheet" href="//cdn.bootcss.com/dropzone/%s/min/%s"' \
                  ' type="text/css">\n' % (version, css_filename)

        if css_url:
            css = '<link rel="stylesheet" href="%s" type="text/css">\n' % css_url
        return Markup(css)

    @staticmethod
    def load_js(version='5.2.0', js_url=None):
        js_filename = 'dropzone.min.js'
        serve_local = current_app.config['DROPZONE_SERVE_LOCAL']

        if serve_local:
            js = '<script src="%s"></script>\n' % url_for('dropzone.static', filename=js_filename)
        else:
            js = '<script src="//cdn.bootcss.com/dropzone/%s/min/%s">' \
                 '</script>\n' % (version, js_filename)

        if js_url:
            js = '<script src="%s"></script>\n' % js_url
        return Markup(js)

    @staticmethod
    def config(redirect_url=None):
        upload_multiple = current_app.config['DROPZONE_UPLOAD_MULTIPLE']
        parallel_uploads = current_app.config['DROPZONE_PARALLEL_UPLOADS']

        if upload_multiple in [True, 'true', 'True', 1]:
            upload_multiple = 'true'
        else:
            upload_multiple = 'false'

        size = current_app.config['DROPZONE_MAX_FILE_SIZE']
        param = current_app.config['DROPZONE_INPUT_NAME']
        redirect_view = current_app.config['DROPZONE_REDIRECT_VIEW']

        if redirect_view is not None or redirect_url is not None:
            redirect_url = redirect_url or url_for(redirect_view)
            redirect_js = '''
            this.on("queuecomplete", function(file) { 
            // Called when all files in the queue finish uploading.
            window.location = "%s";
            });''' % redirect_url
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

        return Markup('''<script>
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
                ''' % (redirect_js, upload_multiple, parallel_uploads, param, size, allowed_type, max_files,
                       default_message, browser_unsupported, invalid_file_type, file_too_big,
                       server_error, max_files_exceeded))

    @staticmethod
    def create(action='', csrf=False, action_view='', **kwargs):
        """Create a Dropzone form with given action.

        .. versionchanged:: 1.4.2
        Added `csrf` parameter to enable CSRF protect.

        :param action: The action attribute in <form>, pass the url which handle uploads.
        :param csrf: Enable CSRF protect or not, same with `DROPZONE_ENABLE_CSRF`.
        :param action_view: The view which handle the post data, deprecated since 1.4.2.
        """
        if action:
            action_url = action
        else:
            action_url = url_for(action_view, **kwargs)

        if csrf or current_app.config['DROPZONE_ENABLE_CSRF']:
            if 'csrf' not in current_app.extensions:
                raise RuntimeError("CSRFProtect is not initialized. It's required to enable CSRF protect, \
                    see docs for more details.")
            csrf_field = render_template_string('<input type="hidden" name="csrf_token" value="{{ csrf_token() }}"/>')
        else:
            csrf_field = ''
        return Markup('''<form action="%s" method="post" class="dropzone" id="myDropzone" 
        enctype="multipart/form-data">%s</form>''' % (action_url, csrf_field))

    @staticmethod
    def style(css):
        """Add css to dropzone.

        :param css: style sheet code.
        """
        return Markup('<style>\n.dropzone{%s}\n</style>' % css)


class Dropzone(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):

        blueprint = Blueprint('dropzone', __name__,
                              static_folder='static',
                              static_url_path=app.static_url_path + '/dropzone')
        app.register_blueprint(blueprint)

        if not hasattr(app, 'extensions'):
            app.extensions = {}
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
        # .. versionadded:: 1.4.1
        app.config.setdefault('DROPZONE_REDIRECT_VIEW', None)

        # Whether to send multiple files in one request.
        # In default, each file will send with a request.
        # Then you can use ``request.files.getlist('paramName')`` to 
        # get a list of uploads.
        # .. versionadded:: 1.4.1
        app.config.setdefault('DROPZONE_UPLOAD_MULTIPLE', False)

        # When ``DROPZONE_UPLOAD_MULTIPLE`` set to True, this will
        # defined how many uploads will handled in per request.
        # .. versionadded:: 1.4.1
        app.config.setdefault('DROPZONE_PARALLEL_UPLOADS', 2)

        # When set to ``True``, it will add a csrf_token hidden field in upload form.
        # You have to install Flask-WTF to make it work properly, see details in docs.
        # .. versionadded:: 1.4.2
        app.config.setdefault('DROPZONE_ENABLE_CSRF', False)

        # messages
        app.config.setdefault('DROPZONE_DEFAULT_MESSAGE', "Drop files here or click to upload.")
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
