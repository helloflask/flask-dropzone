# -*- coding: utf-8 -*-
"""
    :author: Grey Li <withlihui@gmail.com>
    :copyright: (c) 2017 by Grey Li.
    :license: MIT, see LICENSE for more details.
"""
import os
import uuid

from flask import Flask, render_template, request
from flask_dropzone import Dropzone

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config.update(
    UPLOADED_PATH=os.path.join(basedir, 'uploads'),
    # Flask-Dropzone config:
    DROPZONE_ALLOWED_FILE_TYPE='image',
    DROPZONE_MAX_FILE_SIZE=3,
    DROPZONE_MAX_FILES=30,
    DROPZONE_IN_FORM=True,
    DROPZONE_UPLOAD_ON_CLICK=True,
    DROPZONE_UPLOAD_ACTION='handle_upload',  # URL or endpoint
    DROPZONE_UPLOAD_BTN_ID='submit',
)

dropzone = Dropzone(app)


@app.route('/')
def index():
    fake_csrf = uuid.uuid1().get_hex()
    return render_template('index.html', csrf_token=fake_csrf)


@app.route('/upload', methods=['POST'])
def handle_upload():
    # note, request.form.get('title') and others are available here
    csrf = request.form['csrf_token']
    if request.files:
        os.makedirs(os.path.join(app.config['UPLOADED_PATH'], csrf)) # 777 probably aren't good permissions
    for key, f in request.files.items():
        if key.startswith('file'):
            f.save(os.path.join(app.config['UPLOADED_PATH'], csrf, f.filename))
    return '', 204


@app.route('/form', methods=['POST'])
def handle_form():
    title = request.form.get('title')
    description = request.form.get('description')
    csrf = request.form['csrf_token']
    n_files = len(os.listdir(os.path.join(app.config['UPLOADED_PATH'], csrf)))
    return ('file uploaded and form submit<br>title: %s<br>'
            'description: %s<br># files: %s' % (title, description, n_files))


if __name__ == '__main__':
    app.run(debug=True)
