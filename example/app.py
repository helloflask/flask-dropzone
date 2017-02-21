# -*- coding: utf-8 -*-
import os

from flask import Flask, render_template, request
from flask_dropzone import Dropzone

app = Flask(__name__)
dropzone = Dropzone(app)

app.config['UPLOADED_PATH'] = '/upload'
app.config.update(
    DROPZONE_ALLOWED_FILE_TYPE='image',
    DROPZONE_MAX_FILE_SIZE=3,
    DROPZONE_INPUT_NAME='photo',
    DROPZONE_MAX_FILES=30
)


@app.route('/', methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        for f in request.files.getlist('photo'):
            f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
