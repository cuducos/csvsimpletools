# coding: utf-8

from datetime import datetime
from random import randrange
from unipath import Path


def r_name():
    color = ["red", "Blue", "BLACK", "O-ran-ge"]
    tool = ["Hammer", "drill", "Poça", "KNI?FE"]
    r_color = color[randrange(0, len(color))]
    r_tool = tool[randrange(0, len(tool))]
    return '{} {}'.format(r_color, r_tool)


def create_line(i):
    key = '{0:0>6}'.format(i)
    return '{},{}'.format(r_name(), key)


def create_csv(lines):
    content = map(lambda x: create_line(x + 1), range(0, lines))
    return '\n'.join(content)


def filesize(size):
    sizes = {
        9: 'Gb',
        6: 'Mb',
        3: 'Kb',
        0: 'bytes'
    }
    for i in [9, 6, 3, 0]:
        if size >= 10 ** i:
            return '{:.1f}'.format(size / (10.0 ** i)) + sizes[i]
    return '0 %s' % sizes[0]

date_time = datetime.now()
filename = 'sample-{}.csv'.format(date_time.strftime('%Y%m%d%H%M%S'))
handler = Path(filename)
lines = randrange(50 * 10 ** 3, 150 * 10 ** 3)
content = create_csv(lines)
handler.write_file(content)
size = filesize(handler.size())

print '==> {} was created with {} lines ({})'.format(filename, lines, size)
