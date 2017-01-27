import balance

def lambda_handler(event, context):
    if event['request']['type'] == "IntentRequest":
        return intent_request(event['request'])

def intent_request(request):
    intent = request['intent']

    if intent['name'] == "GetBalance":
        return balance.get_balance(intent)

def build_response(output):
    return {
        'version': '1.0',
        'response': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': output
            },
            'card': {
                'type': 'Simple',
                'title': 'Monzo',
                'content': output
            },
            'shouldEndSession': True
        }
    }
