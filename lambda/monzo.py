import balance
import os

def lambda_handler(event, context):
    if event['session']['application']['applicationId'] != os.environ['APP_ID']:
        print "Invalid Application ID"
        return error_response()

    request_type = event['request']['type']

    if request_type == "IntentRequest":
        return intent_request(event['request'])
    elif request_type == "LaunchRequest":
        print "LaunchRequest - No intent provided"
        return build_response("Monzo - Welcome", "Welcome to Monzo! Get started by asking me about your balance or recent transactions.")

def intent_request(request):
    # Temp workaround for OAuth issue
    access_token = os.environ['ACCESS_TOKEN']
    account_id = os.environ['ACCOUNT_ID']
    intent = request['intent']
    intent_name = intent['name']

    if intent_name == "GetBalance":
        return balance.get_balance(access_token, account_id)
    elif intent_name == "GetSpendToday":
        return balance.get_spend_today(access_token, account_id)
    elif intent_name == "AMAZON.NoIntent":
        return build_response("Invalid command", "I'm sorry, I didn't understand your request.")

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

def error_response():
    return build_response("Request error", "I'm sorry, your request could not be completed!")

