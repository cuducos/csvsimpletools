from flask_babel import gettext
from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField, FileRequired
from wtforms import RadioField, SelectField

from csvsimpletools.commands import commands

COMMANDS = tuple((c.function.__name__, c.title) for c in commands)
DELIMITERS = ((",", ","), (";", ";"), ("\t", "tab"))
FILE_VALIDATOR = (
    FileRequired(),
    FileAllowed(("csv", "txt"), gettext("Please use a CSV (.txt or .csv)")),
)


class GetCSV(FlaskForm):
    csv = FileField("CSV File", validators=FILE_VALIDATOR)
    command = RadioField("Commands to execute", choices=COMMANDS)
    input_delimiter = SelectField("Input delimiter", choices=DELIMITERS)
    output_delimiter = SelectField("Output delimiter", choices=DELIMITERS)
