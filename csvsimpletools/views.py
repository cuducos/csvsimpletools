from csv import reader, writer
from tempfile import TemporaryFile

from flask import Blueprint, jsonify, make_response, render_template, request

from csvsimpletools.commands import commands
from csvsimpletools.forms import GetCSV


COMMANDS = {c.function.__name__: c for c in commands}
main = Blueprint(__name__, 'main')


@main.route('/')
@main.route('/<lang>')
def index(lang='en', methods=('GET', 'POST')):

    form = GetCSV()
    if request.method == 'POST':
        return convert(form)

    return render_template('form.html', commands=COMMANDS, form=form)


def convert(form):

    if not form.validate_on_submit():
        return jsonify(form.errors), 422

    requested = form.command.data
    command = COMMANDS.get(form.command.data)
    if not command:
        return jsonify({'error': f'Command {requested} not found'}), 422

    uploaded = request.files.get('csv')
    delimiter = form.input_delimiter.data
    content = command.function(reader(uoloaded, delimiter=delimiter))

    headers = {
        'Content-Type': 'text/csv',
        'Content-Disposition': f'attachment; filename={uploaded.filename}'
    }
    response = make_response(content)
    response.headers.update(headers)
    return response
