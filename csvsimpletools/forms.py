from flask_babel import gettext
from flask_wtf import Form
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms import RadioField, SelectField

from csv_commands import ordered_commands


COMMANDS = tuple((c.method.__name__, c.title) for c in ordered_commands)
DELIMITERS = ((',', ','), (';', ';'), ('\t', 'tab'))
FILE_VALIDATOR = (
    FileRequired(),
    FileAllowed(('csv', 'txt'), gettext('Please use a CSV (.txt or .csv)'))
)


class GetCSV(Form):
    csv = FileField('CSV File', validators=FILE_VALIDATOR)
    command = RadioField('Commands to execute', choices=COMMANDS)
    input_delimiter = SelectField('Input delimiter', choices=DELIMITERS)
    output_delimiter = SelectField('Output delimiter', choices=DELIMITERS)
