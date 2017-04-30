import os

import balance
import card
import response
import transactions


def handler(event, context):
    if event['session']['application']['applicationId'] != os.environ['APP_ID']:
        print("Invalid Application ID")
        return response.error()

    if "accessToken" not in event['session']['user']:
        return response.build("Authentication Error", "I'm sorry, there was a problem authenticating with your Monzo account.")

    access_token = event['session']['user']['accessToken']
    request_type = event['request']['type']

    if request_type == "IntentRequest":
        return intent_request(event['request'], access_token)
    elif request_type == "LaunchRequest":
        print("LaunchRequest - No intent provided")
        return response.build("Welcome", "Welcome to Monzo! Get started by asking me about your balance or recent transactions.")


def intent_request(request, access_token):
    account_id = os.environ['ACCOUNT_ID']
    intent = request['intent']
    intent_name = intent['name']

    print("IntentRequest: %s" % intent_name)

    if intent_name == "GetBalance":
        return balance.get_balance(access_token, account_id)
    elif intent_name == "GetSpendToday":
        return balance.get_spend_today(access_token, account_id)
    elif intent_name == "GetTransactions":
        return transactions.get_transactions(access_token, account_id, intent['slots'])
    elif intent_name == "GetCardStatus":
        return card.get_status(access_token, account_id)
    elif intent_name == "BlockCard":
        return card.block_card(access_token, account_id)
    elif intent_name == "UnblockCard":
        return card.unblock_card(access_token, account_id)
    elif intent_name == "AMAZON.HelpIntent":
        return response.build("Help", "Try asking me about your balance, or recent transactions.")
    else:
        return response.build("Invalid command", "I'm sorry, I didn't understand your request.")
