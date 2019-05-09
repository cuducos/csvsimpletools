import re
from collections import namedtuple
from inspect import signature
from unicodedata import category, normalize

from flask_babel import lazy_gettext as _

fields = ("title", "description", "input", "output", "order", "function")
Command = namedtuple("Command", fields)


def main_command_function(lines, transform):
    count = len(signature(transform).parameters)  # how many args are expected
    for line in lines:
        args = line[:count]
        yield line + [transform(*args)]


def sentence(lines):
    yield from main_command_function(lines, str.capitalize)


def title(lines):
    yield from main_command_function(lines, str.title)


def upper(lines):
    yield from main_command_function(lines, str.upper)


def lower(lines):
    yield from main_command_function(lines, str.lower)


def concatenate(lines):
    yield from main_command_function(lines, lambda x, y: f"{x}{y}")


def special(lines):
    def clean(value):
        return "".join(
            character
            for character in normalize("NFD", value)
            if category(character) != "Mn"
        )

    yield from main_command_function(lines, clean)


def alphanum(lines):
    def clean(value):
        return re.sub("[^a-zA-Z0-9]+", "", value)

    yield from main_command_function(lines, clean)


def sequential(lines):
    for count, line in enumerate(lines, 1):
        yield line + [str(count)]


def dualseq(iterable):
    count = {}
    for line in iterable:
        key, *_ = line
        count[key] = count.get(key, 0) + 1
        yield line + [key, f"{count[key]:0>8}"]


commands = (
    Command(
        _("Sentence Case"),
        _(
            (
                "Add a column to the end of the CSV with the value of the first "
                "column in sentence case."
            )
        ),
        "foo bar,42",
        "foo bar,42,Foo bar",
        1,
        sentence,
    ),
    Command(
        _("Title Case"),
        _(
            (
                "Add a column to the end of the CSV with the value of the first "
                "column in title case."
            )
        ),
        "foo bar,42",
        "foo bar,42,Foo Bar",
        2,
        title,
    ),
    Command(
        _("Upper Case"),
        _(
            (
                "Add a column to the end of the CSV with the value of the first "
                "column in upper case."
            )
        ),
        "foobar,42",
        "foobar,42,FOOBAR",
        3,
        upper,
    ),
    Command(
        _("Lower Case"),
        _(
            (
                "Add a column to the end of the CSV with the value of the first "
                "column in lower case."
            )
        ),
        "FOOBAR,42",
        "FOOBAR,42,foobar",
        4,
        lower,
    ),
    Command(
        _("Concatenate"),
        _(
            (
                "Add a column to the end of the CSV with the value of the first "
                "and second columns concatenated."
            )
        ),
        "foobar,42,None",
        "foobar,42,None,foobar42",
        5,
        concatenate,
    ),
    Command(
        _("Remove Special Chars"),
        _(
            (
                "Add a column to the end of the CSV with the value of the first "
                "column replacing any special character."
            )
        ),
        "föôbàr,42",
        "föôbàr,42,foobar",
        6,
        special,
    ),
    Command(
        _("Alphanumeric Only"),
        _(
            (
                "Add a column to the end of the CSV with the value of the first "
                "column keeping only letters and numbers ."
            )
        ),
        "foo + bar ? 42,42",
        "foo + bar ? 42,42,foobar42",
        7,
        alphanum,
    ),
    Command(
        _("Sequential numbers"),
        _(
            (
                "Add a column to the end of the CSV with a sequential number "
                "(starting with 1, with increment in each row)."
            )
        ),
        "foobar,42",
        "foobar,42,1",
        8,
        sequential,
    ),
    Command(
        _("Dual sequential numbers"),
        _(
            (
                "Add one column to the end of the CSV with a sequential number for"
                "each different first column."
            )
        ),
        "foo,bar\nfoo,etc\nxpto,bar",
        "foo,bar,foo,00000001\nfoo,etc,foo,00000002\nxpto,bar,xpto,00000001",
        9,
        dualseq,
    ),
)
