#!/bin/sh

DIR=$PWD

zip -j9 lambda.zip monzo/*.py
cd $DIR/venv/lib/python2.7/site-packages
find isodate -type file -name "*.py" | xargs zip -9 $DIR/lambda.zip
find urllib3 -type file -name "*.py" | xargs zip -9 $DIR/lambda.zip
