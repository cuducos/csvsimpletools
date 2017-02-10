# CSV Simple Tools

Simple web app to run simple tasks in CSV files — e.g. concatenate, lower case, upper case, sentence case, replace special chars etc.

## Install

1. If you want get your [Python 3.6](http://www.python.org) running under a [virtualenv](https://pypi.python.org/pypi/virtualenv)
1. Install the requirements:<br>
   `$ python -m pip install -r requirements.txt`
1. Create Flask variables:<br>
   `$ export FLASK_APP=csvsimpletools/__init__.py`<br>
1. Optionally turn the debug mode on:<br>
   `$ export FLASK_DEBUG=1`
1. Then start your server:<br>
   `$ flask run`