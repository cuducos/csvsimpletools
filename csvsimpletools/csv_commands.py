# coding: utf-8

import re
from flask.ext.babel import lazy_gettext
from unicodedata import category, normalize

commands = [('sentence', lazy_gettext('Sentence Case')),
            ('title', lazy_gettext('Title Case')),
            ('upper', lazy_gettext('Upper Case')),
            ('lower', lazy_gettext('Lower Case')),
            ('concatenate', lazy_gettext('Concatenate')),
            ('special', lazy_gettext('Remove Special Chars')),
            ('alphanum', lazy_gettext('Alphanumeric Only')),
            ('sequential', lazy_gettext('Add sequential numbers'))]

tooltips = {
    'sentence':
        [lazy_gettext('Add a column to the end of the CSV with the value of the first column in sentence case.'),
         'foo bar,42',
         'foo bar,42,Foo bar'],
    'title':
        [lazy_gettext('Add a column to the end of the CSV with the value of the first column in title case.'),
         'foo bar,42',
         'foo bar,42,Foo Bar'],
    'upper':
        [lazy_gettext('Add a column to the end of the CSV with the value of the first column in upper case.'),
         'foobar,42',
         'foobar,42,FOOBAR'],
    'lower':
        [lazy_gettext('Add a column to the end of the CSV with the value of the first column in lower case.'),
         'FOOBAR,42',
         'FOOBAR,42,foobar'],
    'concatenate':
        [lazy_gettext('Add a column to the end of the CSV with the value of the first and second columns concatenated.'),
         'foobar,42,None',
         'foobar,42,None,foobar42'],
    'special':
        [lazy_gettext('Add a column to the end of the CSV with the value of the first column replacing any special character.'),
         'föôbàr,42',
         'föôbàr,42,foobar'],
    'alphanum':
        [lazy_gettext('Add a column to the end of the CSV with the value of the first column keeping only letters and numbers .'),
         'foo + bar ? 42,42',
         'foo + bar ? 42,42,foobar42'],
    'sequential':
        [lazy_gettext('Add a column to the end of the CSV with a sequential number (starting with 1, with increment in each row).'),
         'foobar,42',
         'foobar,42,1']
}


def sentence(lines):
    output = []
    for line in lines:
        value = line[0]
        new_line = list(line)
        new_line.append(value.capitalize())
        output.append(new_line)
    return output


def title(lines):
    output = []
    for line in lines:
        value = line[0]
        new_line = list(line)
        new_line.append(value.title())
        output.append(new_line)
    return output


def upper(lines):
    output = []
    for line in lines:
        value = line[0]
        new_line = list(line)
        new_line.append(value.upper())
        output.append(new_line)
    return output


def lower(lines):
    output = []
    for line in lines:
        value = line[0]
        new_line = list(line)
        new_line.append(value.lower())
        output.append(new_line)
    return output


def concatenate(lines):
    output = []
    for line in lines:
        value = '{}{}'.format(line[0], line[1])
        new_line = list(line)
        new_line.append(value)
        output.append(new_line)
    return output


def special(lines):
    output = []
    for line in lines:
        v = u'{}'.format(line[0])
        value = ''.join(c for c in normalize('NFD', v) if category(c) != 'Mn')
        new_line = list(line)
        new_line.append(value)
        output.append(new_line)
    return output


def alphanum(lines):
    output = []
    regex = re.compile('[^a-zA-Z0-9]+')
    for line in lines:
        value = line[0]
        new_line = list(line)
        new_line.append(regex.sub('', value))
        output.append(new_line)
    return output


def sequential(lines):
    output = []
    count = 1
    for line in lines:
        new_line = list(line)
        new_line.append(str(count))
        output.append(new_line)
        count = count + 1
    return output
