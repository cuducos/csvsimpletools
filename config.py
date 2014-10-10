# coding: utf-8

from decouple import config

WTF_CSRF_ENABLED = True
SECRET_KEY = config('SECRET_KEY', default='')
CSRF_ENABLED = True
DEBUG = config('DEBUG', default=False, cast=bool)

COMMANDS = [('sentence', 'Sentence Case'),
            ('title', 'Title Case'),
            ('upper', 'Upper Case'),
            ('lower', 'Lower Case'),
            ('concatenate', 'Concatenate'),
            ('special', 'Remove Special Chars'),
            ('alphanum', 'Alphanumeric Only'),
            ('sequential', 'Add sequential numbers')]

TOOLTIPS = {
    'sentence':
        ['Add a column to the end of the CSV with the value of\
         the first column in sentence case.',
         'foo bar,42',
         'foo bar,42,Foo bar'],
    'title':
        ['Add a column to the end of the CSV with the value of\
         the first column in title case.',
         'foo bar,42',
         'foo bar,42,Foo Bar'],
    'upper':
        ['Add a column to the end of the CSV with the value of\
         the first column in upper case.',
         'foobar,42',
         'foobar,42,FOOBAR'],
    'lower':
        ['Add a column to the end of the CSV with the value of\
         the first column in lower case.',
         'FOOBAR,42',
         'FOOBAR,42,foobar'],
    'concatenate':
        ['Add a column to the end of the CSV with the value of\
         the first and second columns concatenated.',
         'foobar,42,None',
         'foobar,42,None,foobar42'],
    'special':
        ['Add a column to the end of the CSV with the value of\
         the first column replacing any special character.',
         'föôbàr,42',
         'föôbàr,42,foobar'],
    'alphanum':
        ['Add a column to the end of the CSV with the value of\
         the first column keeping only letters and numbers .',
         'foo + bar ? 42,42',
         'foo + bar ? 42,42,foobar42'],
    'sequential':
        ['Add a column to the end of the CSV with a sequential\
         number (starting with 1, with increment in each row).',
         'foobar,42',
         'foobar,42,1']
}
