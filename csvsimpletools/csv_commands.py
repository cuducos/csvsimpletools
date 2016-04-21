# coding: utf-8

import operator
import re
from flask.ext.babel import lazy_gettext
from unicodedata import category, normalize

# command definitions

commands = {

    'sentence': {
        'title': lazy_gettext('Sentence Case'),
        'description': lazy_gettext('Add a column to the end of the CSV with the value of the first column in sentence case.'),
        'input': 'foo bar,42',
        'output': 'foo bar,42,Foo bar',
        'order': 1
    },

    'title': {
        'title': lazy_gettext('Title Case'),
        'description': lazy_gettext('Add a column to the end of the CSV with the value of the first column in title case.'),
        'input': 'foo bar,42',
        'output': 'foo bar,42,Foo Bar',
        'order': 2
    },

    'upper': {
        'title': lazy_gettext('Upper Case'),
        'description': lazy_gettext('Add a column to the end of the CSV with the value of the first column in upper case.'),
        'input': 'foobar,42',
        'output': 'foobar,42,FOOBAR',
        'order': 3
    },

    'lower': {
        'title': lazy_gettext('Lower Case'),
        'description': lazy_gettext('Add a column to the end of the CSV with the value of the first column in lower case.'),
        'input': 'FOOBAR,42',
        'output': 'FOOBAR,42,foobar',
        'order': 4
    },

    'concatenate': {
        'title': lazy_gettext('Concatenate'),
        'description': lazy_gettext('Add a column to the end of the CSV with the value of the first and second columns concatenated.'),
        'input': 'foobar,42,None',
        'output': 'foobar,42,None,foobar42',
        'order': 5
    },

    'special': {
        'title': lazy_gettext('Remove Special Chars'),
        'description': lazy_gettext('Add a column to the end of the CSV with the value of the first column replacing any special character.'),
        'input': 'föôbàr,42',
        'output': 'föôbàr,42,foobar',
        'order': 6
    },

    'alphanum': {
        'title': lazy_gettext('Alphanumeric Only'),
        'description': lazy_gettext('Add a column to the end of the CSV with the value of the first column keeping only letters and numbers .'),
        'input': 'foo + bar ? 42,42',
        'output': 'foo + bar ? 42,42,foobar42',
        'order': 7
    },

    'sequential': {
        'title': lazy_gettext('Sequential numbers'),
        'description': lazy_gettext('Add a column to the end of the CSV with a sequential number (starting with 1, with increment in each row).'),
        'input': 'foobar,42',
        'output': 'foobar,42,1',
        'order': 8
    },

    'dualseq': {
        'title': lazy_gettext('Dual sequential numbers'),
        'description': lazy_gettext('Add two columns to the end of the CSV with a sequential number for each different first and second column.'),
        'input': 'foo,bar\nfoo,etc\nxpto,bar',
        'output': 'foo,bar,foo,00000001\nfoo,etc,foo,00000002\nxpto,bar,xpto,00000001',
        'order': 9
    }
}


def get_command_list():
    commands_order = dict()
    for command in commands.keys():
        commands_order[command] = commands[command]['order']
    sorted_commands = sorted(commands_order.items(),
                             key=operator.itemgetter(1))
    return [c[0] for c in sorted_commands]

command_list = get_command_list()

# command methods

def sentence(lines):
    output = list()
    for line in lines:
        value = line[0]
        new_line = list(line)
        new_line.append(value.capitalize())
        output.append(new_line)
    return output


def title(lines):
    output = list()
    for line in lines:
        value = line[0]
        new_line = list(line)
        new_line.append(value.title())
        output.append(new_line)
    return output


def upper(lines):
    output = list()
    for line in lines:
        value = line[0]
        new_line = list(line)
        new_line.append(value.upper())
        output.append(new_line)
    return output


def lower(lines):
    output = list()
    for line in lines:
        value = line[0]
        new_line = list(line)
        new_line.append(value.lower())
        output.append(new_line)
    return output


def concatenate(lines):
    output = list()
    for line in lines:
        value = '{}{}'.format(line[0], line[1])
        new_line = list(line)
        new_line.append(value)
        output.append(new_line)
    return output


def special(lines):
    output = list()
    for line in lines:
        v = u'{}'.format(line[0])
        value = ''.join(c for c in normalize('NFD', v) if category(c) != 'Mn')
        new_line = list(line)
        new_line.append(value)
        output.append(new_line)
    return output


def alphanum(lines):
    output = list()
    regex = re.compile('[^a-zA-Z0-9]+')
    for line in lines:
        value = line[0]
        new_line = list(line)
        new_line.append(regex.sub('', value))
        output.append(new_line)
    return output


def sequential(lines):
    output = list()
    count = 1
    for line in lines:
        new_line = list(line)
        new_line.append(str(count))
        output.append(new_line)
        count = count + 1
    return output


def dualseq(lines):

    # support vars
    output = list(lines)
    grouped = dict()
    index = 1

    # first loop: group all values by the first field
    for line in lines:
        try:
            grouped[line[0]]['values'].append(line[1])
        except KeyError:
            grouped[line[0]] = {
                'index': index,
                'values': [line[1]],
                'count': 1
            }
            index += 1

    # second loop: create the codes
    for index, line in enumerate(output):
        obj = grouped[line[0]]
        second_code = '{0:0>8}'.format(obj['count'])
        output[index].extend([line[0], second_code])
        obj['count'] += 1

    return output
