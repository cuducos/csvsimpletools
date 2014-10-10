# coding: utf-8
import csv_commands
import sys
from csv import reader, writer
from csvsimpletools import app
from flask import make_response, render_template, request
from forms import GetCSV
from tempfile import TemporaryFile

reload(sys)
sys.setdefaultencoding('utf-8')


@app.route('/')
def index():
    return render_template('form.html',
                           commands=app.config['COMMANDS'],
                           tooltips=app.config['TOOLTIPS'],
                           form=GetCSV())


@app.route('/result', methods=('GET', 'POST'))
def result():

    # load form
    form = GetCSV()

    # if uploaded info is valid, generate new CSV accordingly
    if form.validate_on_submit():

        # copy uploaded content to a temp file
        uploaded = request.files['csv']
        with TemporaryFile() as temp1:
            temp1.write(uploaded.read())
            temp1.seek(0)
            temp1.flush()
            lines = list(reader(temp1))

        # parse and process the CSV
        command = form.command.data
        if command == 'sentence':
            new = csv_commands.sentence(lines)
        elif command == 'title':
            new = csv_commands.title(lines)
        elif command == 'upper':
            new = csv_commands.upper(lines)
        elif command == 'lower':
            new = csv_commands.lower(lines)
        elif command == 'concatenate':
            new = csv_commands.concatenate(lines)
        elif command == 'special':
            new = csv_commands.special(lines)
        elif command == 'alphanum':
            new = csv_commands.alphanum(lines)
        elif command == 'sequential':
            new = csv_commands.sequential(lines)
        else:
            new = list(lines)

        # create CSV for download
        with TemporaryFile() as temp2:
            output = writer(temp2)
            output.writerows(new)
            temp2.seek(0)
            content = temp2.read()

        # generate response
        f = uploaded.filename
        r = make_response(content)
        r.headers["Content-Type"] = "text/csv"
        r.headers["Content-Disposition"] = 'attachment; filename={}'.format(f)
        return r

    # else, return error
    return 'Error(s): '.format(form.errors)
