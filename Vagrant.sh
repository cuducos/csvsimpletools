#!/usr/bin/env bash

# Python
apt-get update
apt-get install -y python-setuptools git
easy_install pip

# install project dependencies
pip install -r /vagrant/requirements.txt

# install dev tools
apt-get install -y sqlite3
pip install ipython
