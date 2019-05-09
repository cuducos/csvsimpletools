import csv
from pathlib import Path
from tempfile import TemporaryDirectory

from flask import Blueprint, jsonify, make_response, render_template, request

from csvsimpletools.commands import commands
from csvsimpletools.forms import GetCSV

COMMANDS = {c.function.__name__: c for c in commands}
main = Blueprint(__name__, "main")


@main.route("/", methods=("GET", "POST"))
@main.route("/<lang>", methods=("GET", "POST"))
def index(lang="en"):
    form = GetCSV()
    if request.method == "POST":
        return convert(form)
    return render_template("form.html", lang=lang, commands=COMMANDS, form=form)


def convert(form):
    if not form.validate_on_submit():
        return jsonify(form.errors), 422

    command = COMMANDS.get(form.command.data)
    if not command:
        return jsonify({"error": f"Command {form.command.data} not found"}), 422

    uploaded = request.files["csv"]
    data = convert_csv(uploaded.read(), command.function, form.input_delimiter.data)

    response = make_response(data)
    response.headers.add_header("Content-Type", "text/csv")
    response.headers.add_header(
        "Content-Disposition", f"attachment; filename={uploaded.filename}"
    )
    return response


def convert_csv(csv_data_as_bytes, func, delimiter=","):
    with TemporaryDirectory() as tmp:
        input_, output = Path(tmp, "input"), Path(tmp, "output")
        input_.write_bytes(csv_data_as_bytes)
        with input_.open() as read, output.open("w") as write:
            reader = csv.reader(read, delimiter=delimiter)
            lines = tuple(line for line in reader)
            writer = csv.writer(write, delimiter=delimiter)
            writer.writerows(func(lines))
        return output.read_text()
