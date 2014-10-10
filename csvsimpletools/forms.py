# coding: utf-8
from csvsimpletools import app
from flask_wtf import Form
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import RadioField


class GetCSV(Form):

    csv = FileField('CSV File',
                    validators=[FileRequired(),
                                FileAllowed(['csv'],
                                            'Please, use .csv files only.')])

    command = RadioField('Commands to execute', choices=app.config['COMMANDS'])
