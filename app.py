from flask import Flask, render_template, url_for, jsonify, flash, request, redirect
from werkzeug.utils import secure_filename
import os
import urllib.request

UPLOAD_FOLDER = './uploaded_files/'

app = Flask(__name__)
app_name = 'CEQuery'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.secret_key = "secret key"
ALLOWED_EXTENSIONS = set(['csv'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
@app.route('/upload_file')
def upload_file():
    title = 'CEQuery - Upload File'
    return render_template('upload_file.html', title=title, app_name=app_name), 200


@app.route('/', methods=['POST'])
def uploader():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('There are no files to be uploaded')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash('File successfully uploaded - ' + filename)
            return redirect('/results')
        else:
            flash('Only csv files are allowed to be uploaded')
            return redirect('request.url')


@app.route('/results')
def results():
    title = 'CEQuery - Results'
    return render_template('results.html', title=title, app_name=app_name), 200


if __name__ == '__main__':
    app.run()
