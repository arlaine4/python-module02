#!/bin/bash

echo "Upgrading pip"
python3 -m pip install --upgrade pip --user

echo "Installing setuptools"
python3 -m pip install setuptools --user

echo "Installing wheel"
python3 -m pip install wheel --user

echo "Creating archive my_minipack-1.0.0.tar.gz"
python3 setup.py sdist --formats gztar

echo "Creating my_minipack-1.0.0-py3-none-any.whl"
python3 setup.py bdist_wheel

# Now we can run either :
#   python3 -m pip install ./dist/my_minipack-1.0.0.tar.gz
#   python3 -m pip install ./dist/my_minipack-1.0.0-py3-none-any.whl
# and then run : python3 -m pip list
# and then     : python3 -m pip show -v my_minipack