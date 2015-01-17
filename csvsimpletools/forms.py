# coding: utf-8
from csv_commands import command_list, commands
from flask.ext.babel import gettext
from flask_wtf import Form
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import RadioField, SelectField


class GetCSV(Form):

    csv = FileField(
        'CSV File',
        validators=[FileRequired(),
                    FileAllowed(['csv', 'txt'],
                    gettext('Please, a CSV file (.txt or .csv)'))])
    input_delimiter = SelectField('Input delimiter',
                                  choices=[(',', ','),
                                           (';', ';'),
                                           ('\t', 'tab')])
    output_delimiter = SelectField('Output delimiter',
                                   choices=[(',', ','),
                                            (';', ';'),
                                            ('\t', 'tab')])
    command = RadioField('Commands to execute',
                         choices=[(c, commands[c]) for c in command_list])
