# coding: utf-8
from csv_commands import commands
from flask.ext.babel import gettext
from flask_wtf import Form
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import RadioField


class GetCSV(Form):

    csv = FileField(
        'CSV File',
        validators=[FileRequired(),
                    FileAllowed(['csv'],
                    gettext('Please, use .csv files only.'))])

    command = RadioField('Commands to execute', choices=commands)
