zip:
	./zip.sh

test:
	nosetests

update-lambda: zip
	aws lambda update-function-code --function-name alexa-monzo --zip-file fileb://lambda.zip

venv:
	virtualenv --no-site-packages venv && source venv/bin/activate && pip install -r requirements.txt
