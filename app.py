import uuid
from flask import Flask, render_template, url_for, jsonify, flash, request, redirect, session, send_from_directory
from werkzeug.utils import secure_filename
import os
from pandas import *
from numpy import nan as Nan
import pandas as pd
import re
from textblob import TextBlob
import xlrd


UPLOAD_FOLDER = './uploaded_files/'
OUTPUT_FOLDER = './output_files/'
DOMAINS_DICT = './domains_dictionary'


app = Flask(__name__)
app_name = 'CEQuery'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOMAINS_DICT'] = DOMAINS_DICT
app.config['OUTPUT_FOLDER'] = OUTPUT_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 4 * 1024 * 1024
app.secret_key = os.urandom(24)
ALLOWED_EXTENSIONS = set(['xlsx'])


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
            now = datetime.now()
            timestamp = datetime.timestamp(now)
            uniqueid = str(uuid.uuid4())
            filetosave = uniqueid + '_' + str(timestamp) + '_' + filename
            fileloc = os.path.join(app.config['UPLOAD_FOLDER'], filetosave)
            file.save(fileloc)
            outputfilename = 'output_' + os.path.splitext(filetosave)[0] + '.csv'
            outloc = os.path.join(app.config['OUTPUT_FOLDER'], outputfilename)
            session['outputfile'] = outputfilename
            session['outloc'] = outloc
            session['fileloc'] = fileloc
            return results()
        else:
            flash('Only xlsx files are allowed to be uploaded')
            return redirect(request.url)


@app.route('/download_output/')
def downloader():
    if 'outputfile' in session:
        return send_from_directory(app.config['OUTPUT_FOLDER'], session['outputfile'], as_attachment=True), 200
    else:
        return 'error', 404


def results():
    title = 'Results'
    domains, assessment, course, outcomes, staff, support = getResults(session['fileloc'], session['outloc'])
    return render_template('results.html', title=title, app_name=app_name, overall=domains, assessment=assessment, course=course, outcomes=outcomes, staff=staff, support=support), 200


def getdictionary(domains_file):
    xls = ExcelFile(domains_file)  # synonyms for domains
    df = xls.parse(xls.sheet_names[0])
    dm = df.iloc[:, [0, 7, 12, 18, 24]]
    sd1 = df.iloc[:, 1:7]
    sd2 = df.iloc[:, 8:12]
    sd3 = df.iloc[:, 13:18]
    sd4 = df.iloc[:, 19:24]
    sd5 = df.iloc[:, 25:31]
    sd = [sd1, sd2, sd3, sd4, sd5]
    # print(dm)
    return sd, dm


def getreviews(comments_file):
    xls = ExcelFile(comments_file)
    df1 = xls.parse(xls.sheet_names[0])
    # print(df1)
    return df1


def dandsd(df1, dm, sd):
    St = df1['IMPROVE'].tolist()
    li = dm.columns.tolist()
    for x in St:
        St1 = x
        a = []
        cc = []
        aa, bb = np.where(df1.values == St1)
        cou = 0
        tokens = [t.strip() for t in re.findall(r'\b.*?\S.*?(?:\b|$)', St1.lower())]
        for y in tokens:
            cou = cou + 1
            if (y == "," or y == "." or y == "!" or y == "?" or y == ";"):
                cou = cou - 1
            else:
                s = (dm == y).any()
                p = s.index[s]
                if (p.any() != 0):
                    if (len(p) > 1):
                        for i in p:
                            a.append(str(i))
                    else:
                        a.append(str(p[0]))
        a = np.unique(a)
        r, c = df1.shape
        if (len(a) != 0):
            df1.at[aa[0], bb[0] + 1] = a[0]
            for i in range(len(a) - 1):
                r1, c1 = df1.shape
                df1.at[r1, "IMPROVE"] = St1
                df1.at[r1, 1] = a[i + 1]
        else:
            df1.at[aa[0], bb[0] + 1] = "unkonwn"
            df1.at[aa[0], bb[0] + 2] = "unkonwn"
    df1 = df1.sort_values('IMPROVE')
    df1 = df1.reset_index(drop=True)
    # print(df1)
    r, c = df1.shape
    for i in range(r):
        countf = -1
        for xy in li:
            countf = countf + 1
            # print(countf)
            if (df1.iat[i, 1] == xy):
                tokens = [t.strip() for t in re.findall(r'\b.*?\S.*?(?:\b|$)', df1.iat[i, 0].lower())]
                b = []
                for y in tokens:
                    cou = cou + 1
                    if (y == "," or y == "." or y == "!" or y == "?" or y == ";"):
                        cou = cou - 1
                    else:
                        s = (sd[countf] == y).any()
                        p = s.index[s]
                        if (p.any() != 0):
                            if (len(p) > 1):
                                for k in p:
                                    b.append(str(k))
                            else:
                                b.append(str(p[0]))
                b = np.unique(b)
                if (len(b) != 0):
                    df1.at[i, 2] = b[0]
                    for j in range(len(b) - 1):
                        r1, c1 = df1.shape
                        df1.at[r1, "IMPROVE"] = df1.iat[i, 0]
                        df1.at[r1, 1] = df1.iat[i, 1]
                        df1.at[r1, 2] = b[j + 1]
                else:
                    df1.at[i, 2] = "unkonwn"

    df1 = df1.sort_values('IMPROVE')
    df1 = df1.reset_index(drop=True)
    # print(df1)
    return (df1)


def getsentiment(df1):
    stemmed_sentences = df1['IMPROVE'].tolist()
    count = -1
    for row in stemmed_sentences:
        count = count + 1
        sentence_analysis = []
        analysis = TextBlob(row)
        a = analysis.sentiment
        if a.polarity >= 0.1:
            df1.at[count, 3] = "positive"
        else:
            df1.at[count, 3] = "negative"

    return df1


def store(df, url):
    df.columns = ['Comments', 'Domain', 'SUB-DOMAIN', 'SENTIMENT']
    df.to_csv(url)


def createResultObj(newdf):
    newdf.columns = ['IMPROVE', 'DOMAIN', 'SUBDOMAIN', 'SENTIMENT']

    domains = {
        'chartTitle': 'Overall Results across all Domains',
        'labels': [],
        'positive': [],
        'negative': [],
        'both': []
    }

    assessment = {
        'chartTitle': 'Results for Comments on Assessment',
        'labels': [],
        'positive': [],
        'negative': [],
        'both': []
    }

    course = {
        'chartTitle': 'Results for Comments on Course',
        'labels': [],
        'positive': [],
        'negative': [],
        'both': []
    }

    outcomes = {
        'chartTitle': 'Results for Comments on Outcomes',
        'labels': [],
        'positive': [],
        'negative': [],
        'both': []
    }

    staff = {
        'chartTitle': 'Results for Comments on Staff',
        'labels': [],
        'positive': [],
        'negative': [],
        'both': []
    }

    support = {
        'chartTitle': 'Results for Comments on Support',
        'labels': [],
        'positive': [],
        'negative': [],
        'both': []
    }

    g1 = newdf.groupby(["DOMAIN", "SUBDOMAIN", "SENTIMENT"]).count().reset_index()
    domnames = g1.DOMAIN.unique()

    for dom in domnames:
        dpcount = 0
        dncount = 0
        domains['labels'].append(dom)
        sdomnames = g1.query('DOMAIN == @dom').SUBDOMAIN.unique()
        for sdom in sdomnames:
            tp = g1.query('DOMAIN == @dom and SUBDOMAIN == @sdom and SENTIMENT == "positive"').IMPROVE.sum()
            tn = g1.query('DOMAIN == @dom and SUBDOMAIN == @sdom and SENTIMENT == "negative"').IMPROVE.sum()
            dpcount += tp
            dncount += tn
            if dom == "ASSESSMENT":
                assessment['labels'].append(sdom)
                assessment['positive'].append(int(tp))
                assessment['negative'].append(int(tn))
                assessment['both'].append(int(tn)+int(tp))
            elif dom == "COURSE/UNIT DESIGN":
                course['labels'].append(sdom)
                course['positive'].append(int(tp))
                course['negative'].append(int(tn))
                course['both'].append(int(tn) + int(tp))
            elif dom == "OUTCOMES":
                outcomes['labels'].append(sdom)
                outcomes['positive'].append(int(tp))
                outcomes['negative'].append(int(tn))
                outcomes['both'].append(int(tn) + int(tp))
            elif dom == "STAFF":
                staff['labels'].append(sdom)
                staff['positive'].append(int(tp))
                staff['negative'].append(int(tn))
                staff['both'].append(int(tn) + int(tp))
            elif dom == "SUPPORT":
                support['labels'].append(sdom)
                support['positive'].append(int(tp))
                support['negative'].append(int(tn))
                support['both'].append(int(tn) + int(tp))
        domains['positive'].append(int(dpcount))
        domains['negative'].append(int(dncount))
        domains['both'].append(int(dpcount) + int(dncount))
    return domains, assessment, course, outcomes, staff, support


def getResults(fileloc, outloc):
    domainsDictFilename = "Domains-and-subdomains.xlsx"
    sd, dm = getdictionary(os.path.join(app.config['DOMAINS_DICT'], domainsDictFilename))
    df1 = getreviews(fileloc)
    df1 = dandsd(df1, dm, sd)
    df1 = getsentiment(df1)
    store(df1, outloc)
    domains, assessment, course, outcomes, staff, support = createResultObj(df1)
    return domains, assessment, course, outcomes, staff, support


if __name__ == '__main__':
    app.run()
