zip:
	zip -j lambda.zip lambda/*.py

update-lambda: zip
	aws lambda update-function-code --function-name alexa-monzo --zip-file fileb://lambda.zip
