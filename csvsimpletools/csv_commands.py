# coding: utf-8

import re
from unicodedata import category, normalize


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
