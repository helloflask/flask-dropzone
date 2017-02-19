# -*- coding: utf-8 -*-
from distutils.version import StrictVersion
from jinja2 import Markup
from flask import current_app


#: defined normal file type
allowed_file = {
        'default': 'image/*, audio/*, video/*, text/*, application/*',
        'image': 'image/*',
        'audio': 'audio/*',
        'video': 'video/*',
        'text': 'text/*',
        'app': 'application/*'
    }


class _dropzone(object):

    @staticmethod
    def include_dropzone(version='4.3.0', local_js=False):
        js = ''
        size = current_app.config['DROPZONE_MAX_FILE_SIZE']
        param = current_app.config['DROPZONE_INPUT_NAME']
        allowed_type = current_app.config['DROPZONE_ALLOWED_FILE']
        if local_js == True:
            js = '<script src="%s"></script>\n' % local_js
        elif version is not None:
            js_filename = 'dropzone.js'
            js = '<script src="//cdn.bootcss.com/dropzone/%s/%s">' \
                '</script>\n' % (version, js_filename)
        return Markup('''%s<script>
var cleanFilename = function (name) {
   return name.toLowerCase().replace(/[^\w]/gi, '');
};
Dropzone.options.myDropzone = {
  paramName: "%s", // The name that will be used to transfer the file
  maxFilesize: %d, // MB
  acceptedFiles: "%s",
  // renameFilename: cleanFilename,
  accept: function(file, done) {
    if (file.name == "justinbieber.jpg") {
      done("Naha, you don't.");
    }
    else { done(); }
  }
};
        </script>
        ''' % (js, param, size, allowed_type))


class Dropzone(object):
    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        if not hasattr(app, 'extensions'):
            app.extesions = {}
        app.extensions['dropzone'] = _dropzone
        app.context_processor(self.context_processor)

        app.config.setdefault('DROPZONE_SERVE_LOCAL', False)
        app.config.setdefault('DROPZONE_MAX_FILE_SIZE', 2)
        app.config.setdefault('DROPZONE_INPUT_NAME', 'file')
        app.config.setdefault('DROPZONE_ALLOWED_FILE', allowed_file['default'])

    @staticmethod
    def context_processor():
        return {
            'dropzone': current_app.extensions['dropzone']
        }

