Configuration
=============

Register Configuration
-----------------------

Except ``DROPZONE_SERVE_LOCAL``, when you use other configuration variable,
you have to call ``dropzone.config()`` in template to make them register with Dropzone:

.. code-block:: jinja

   <body>
       ...
       {{ dropzone.config() }}
   </body>

.. tip:: Call this method after ``dropzone.load_js()`` or ``<script>`` that include Dropzonejs.

Available Configuration
------------------------

The supported list of config options is shown below:

============================= ====================================================================== ============================================================================================================================================
            Name                                     Default Value                                                                                 Info
============================= ====================================================================== ============================================================================================================================================
DROPZONE_SERVE_LOCAL          ``False`` 	                                                         Default to retrieve dropzone.js from CDN
DROPZONE_MAX_FILE_SIZE 	      ``3`` 	                                                             Max allowed file size. unit: MB
DROPZONE_INPUT_NAME 	      ``file``                                                               The name attribute in ``<input>`` (i.e. ``<input type="file" name="file">``)
DROPZONE_ALLOWED_FILE_CUSTOM  ``False``      	                                                     See detail below
DROPZONE_ALLOWED_FILE_TYPE 	  ``'default'``      	                                                 See detail below
DROPZONE_MAX_FILES 	          ``'null'`` 	                                                         The max files user can upload once
DROPZONE_DEFAULT_MESSAGE 	  ``"Drop files here to upload"`` 	                                     Message displayed on drop area, you can write HTML here (e.g. ``Drop files here<br>Or<br><button type="button">Click to Upload</button>``)
DROPZONE_INVALID_FILE_TYPE 	  ``"You can't upload files of this type."`` 	                         Error message
DROPZONE_FILE_TOO_BIG         ``"File is too big {{filesize}}. Max filesize: {{maxFilesize}}MiB."``  Error message
DROPZONE_SERVER_ERROR 	      ``'"Server error: {{statusCode}}"'`` 	                                 Error message
DROPZONE_BROWSER_UNSUPPORTED  ``"Your browser does not support drag'n'drop file uploads."`` 	     Error message
DROPZONE_MAX_FILE_EXCEED 	  ``"Your can't upload any more files."`` 	                             Error message
DROPZONE_UPLOAD_MULTIPLE 	  ``False`` 	                                                         Whether to send multiple files in one request.
DROPZONE_PARALLEL_UPLOADS 	  ``2`` 	                                                             How many uploads will handled in per request when ``DROPZONE_UPLOAD_MULTIPLE set`` to ``True``.
DROPZONE_REDIRECT_VIEW 	      ``None`` 	                                                             The view to redirect when upload was completed. If you want pass an URL, usually when your view accepts variable, you can pass it with ``redirect_url`` keyword in template: ``{{ dropzone.config(redirect_url=url_for('endpoint', foo=bar)) }}``.
DROPZONE_ENABLE_CSRF 	      ``False`` 	                                                         Enable CSRF protect, see detail below
DROPZONE_TIMEOUT 	          ``None`` 	                                                             The timeout to cancel upload request in millisecond, default to ``30000`` (30 second). Set a large number if you need to upload large file.
============================= ====================================================================== ============================================================================================================================================

File Type Filter
------------------

Just set ``DROPZONE_ALLOWED_FILE_TYPE`` to one of ``default``,
``image``, ``audio``, ``video``, ``text``, ``app``, for example:

.. code-block:: py

    app.config['DROPZONE_ALLOWED_FILE_TYPE'] = 'image'

If you want to set the allowed file type by yourself, you need to set
``DROPZONE_ALLOWED_FILE_CUSTOM`` to ``True``, then add mime type or file
extensions to ``DROPZONE_ALLOWED_FILE_TYPE``, such as:

.. code-block:: python

    app.config['DROPZONE_ALLOWED_FILE_CUSTOM'] = True
    app.config['DROPZONE_ALLOWED_FILE_TYPE'] = 'image/*, .pdf, .txt'

Consult the `dropzone.js documentation <http://dropzonejs.com/>`__ for
details on these options.


Custom Configuration String
----------------------------

Sometimes you may need more flexible, you can use ``custom_init``and ``custom_options``
to pass custom JavaScript code:

.. code-block:: jinja

    {{ dropzone.config(custom_init='dz = this;document.getElementById("upload-btn").addEventListener("click", function handler(e) {dz.processQueue();});',
                     custom_options='autoProcessQueue: false, addRemoveLinks: true, parallelUploads: 20,') }}

The code pass with ``custom_init`` will into ``init: function() {}``, the code pass with ``custom_options`` will into
``Dropzone.options.myDropzone = {}``. See the full list of available configuration settings on
`Dropzone documentation <https://www.dropzonejs.com/#configuration>`__.

Overwriting Global Configuration
----------------------------------

Sometimes you may want to use different configuration for multiple drop area on different pages, in this case, you can
pass the specific keyword arguments into ``dropzone.config()`` directly.

The keyword arguments should mapping the corresponding configration variable in this way:

- DROPZONE_DEFAULT_MESSAGE --> default_message
- DROPZONE_TIMEOUT --> timeout
- DROPZONE_ALLOWED_FILE_TYPE --> allowed_file_type
- etc

example:

.. code-block:: jinja

    {{ dropzone.config(max_files=10, timeout=10000, default_message='Drop here!') }}

In the end, the keyword argument you pass will overwrite the corresponding configurations.
