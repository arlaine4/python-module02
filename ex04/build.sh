#!/bin/bash

# Command to run to activate virtual_env
# python3 -m venv tmp_env && source tmp_env/bin/activate

echo "Upgrading pip"
python3 -m pip install --upgrade pip

echo "Installing setuptools"
python3 -m pip install setuptools

echo "Installing wheel"
python3 -m pip install wheel

echo "Creating archive my_minipack-1.0.0.tar.gz"
python3 setup.py sdist --formats gztar

echo "Creating my_minipack-1.0.0-py3-none-any.whl"
python3 setup.py bdist_wheel

echo "Installing my_minipack"
python3 -m pip install ./dist/my_minipack-1.0.0.tar.gz

# Now we can run :
#              : python3 -m pip list
# and then     : python3 -m pip show -v my_minipack