# -*- coding: utf-8 -*-
__author__ = 'lihui'
import  os

from flask import Flask, render_template, request
from flask_dropzone import Dropzone

app = Flask(__name__)
dropzone = Dropzone(app)
app.config['UPLOADED_PATH'] = os.getcwd() + '/upload'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        for f in request.files.getlist('file'):
            f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
    return 'Redirect to here'

if __name__ == '__main__':
    app.run(debug=True)
