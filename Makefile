DIR = $(shell pwd)

zip:
	zip -j9 lambda.zip monzo/*.py
	cd venv/lib/python2.7/site-packages/ && zip -9 $(DIR)/lambda.zip isodate/*.py

test:
	nosetests --with-coverage

update-lambda: zip
	aws lambda update-function-code --function-name alexa-monzo --zip-file fileb://lambda.zip

venv:
	virtualenv --no-site-packages venv && source venv/bin/activate && pip install -r requirements.txt
