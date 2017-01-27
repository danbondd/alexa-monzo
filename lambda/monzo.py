import balance
import os

def lambda_handler(event, context):
    if event['session']['application']['applicationId'] != os.environ['APP_ID']:
        # Need to log and do something better here!
        raise ValueError("Invalid Application ID")

    accessToken = ""

    if event['request']['type'] == "IntentRequest":
        return intent_request(event['request'], accessToken)

def intent_request(request, accessToken):
    intent = request['intent']

    if intent['name'] == "GetBalance":
        return balance.get_balance(intent, accessToken)

def build_response(title, output):
    return {
        'version': '1.0',
        'response': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': output
            },
            'card': {
                'type': 'Simple',
                'title': title,
                'content': output
            },
            'shouldEndSession': True
        }
    }
