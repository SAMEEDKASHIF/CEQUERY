from flask import Flask, render_template, url_for, jsonify, flash, request, redirect, session
from werkzeug.utils import secure_filename
import os
import urllib.request

UPLOAD_FOLDER = './uploaded_files/'

app = Flask(__name__)
app_name = 'CEQuery'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
app.secret_key = os.urandom(24)
ALLOWED_EXTENSIONS = set(['csv'])


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
@app.route('/upload_file')
def upload_file():
    title = 'Upload File'
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
            overall, assessment, course, outcomes, staff, support = sentimentAnalysisMain(filename)
            return results(overall, assessment, course, outcomes, staff, support)
        else:
            flash('Only csv files are allowed to be uploaded')
            return redirect(request.url)


def results(overall, assessment, course, outcomes, staff, support):
    title = 'Results'
    return render_template('results.html', title=title, app_name=app_name, overall=overall, assessment=assessment, course=course, outcomes=outcomes, staff=staff, support=support), 200


def sentimentAnalysisMain(filename):
    #This is the function where the main code for sentiment analysis will go. This will return a data object containing results for sentiment analysis.
    domains = {
        'summary': {
            'chartTitle': 'Overall Results across all Domains',
            'labels': ['Assessment', 'Course', 'Outcomes', 'Staff', 'Support'],
            'positive': [15, 18, 9, 6, 19],
            'negative': [25, 20, 10, 54, 19]
        }
    }

    assessment = {
        'summary': {
            'chartTitle': 'Results for Comments on Assessment',
            'labels': ['Assessment', 'Course', 'Outcomes', 'Staff', 'Support'],
            'positive': [15, 18, 9, 6, 19],
            'negative': [25, 20, 10, 54, 19]
        }
    }

    course = {
        'summary': {
            'chartTitle': 'Results for Comments on Course',
            'labels': ['Assessment', 'Course', 'Outcomes', 'Staff', 'Support'],
            'positive': [15, 18, 9, 6, 19],
            'negative': [25, 20, 10, 54, 19]
        }
    }

    outcomes = {
        'summary': {
            'chartTitle': 'Results for Comments on Outcomes',
            'labels': ['Assessment', 'Course', 'Outcomes', 'Staff', 'Support'],
            'positive': [15, 18, 9, 6, 19],
            'negative': [25, 20, 10, 54, 19]
        }
    }

    staff = {
        'summary': {
            'chartTitle': 'Results for Comments on Staff',
            'labels': ['Assessment', 'Course', 'Outcomes', 'Staff', 'Support'],
            'positive': [15, 18, 9, 6, 19],
            'negative': [25, 20, 10, 54, 19]
        }
    }

    support = {
        'summary': {
            'chartTitle': 'Results for Comments on Support',
            'labels': ['Assessment', 'Course', 'Outcomes', 'Staff', 'Support'],
            'positive': [15, 18, 9, 6, 19],
            'negative': [25, 20, 10, 54, 19]
        }
    }

    return domains, assessment, course, outcomes, staff, support


if __name__ == '__main__':
    app.run()
