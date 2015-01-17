# coding: utf-8
import csv_commands
import sys
from csv import reader, writer
from csvsimpletools import app, babel
from flask import g, make_response, redirect, render_template, request
from forms import GetCSV
from tempfile import TemporaryFile

reload(sys)
sys.setdefaultencoding('utf-8')


@app.route('/')
def deafult_language():
        return redirect('/en')


@app.route('/<lang>')
def index():
    return render_template('form.html',
                           commands=csv_commands.commands,
                           tooltips=csv_commands.tooltips,
                           languages=app.config['LANGUAGES'],
                           lang=g.get('lang', 'en'),
                           form=GetCSV())


@app.route('/<lang>/result', methods=('GET', 'POST'))
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
        if command in csv_commands.tooltips.keys():
            new = eval('csv_commands.{}(lines)'.format(command))
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
    return 'Error(s): {}'.format(form.errors)


@app.before_request
def before():
    if request.view_args and 'lang' in request.view_args:
        allow = app.config['LANGUAGES'].keys()
        user_choice = request.view_args['lang']
        if user_choice in allow:
            g.lang = user_choice
        else:
            g.lang = request.accept_languages.best_match(allow)
        request.view_args.pop('lang')


@babel.localeselector
def get_locale():
    return g.get('lang', 'en')
