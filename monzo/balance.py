import api
import response
import utils

def get_balance(access_token, account_id):
    res = balance_request(access_token, account_id)
    if res == None:
        return response.error()

    output = "Your balance is %s" % utils.speakable_currency(res['balance'])
    return response.build("Get Balance", output)

def get_spend_today(access_token, account_id):
    res = balance_request(access_token, account_id)
    if res == None:
        return response.error()

    output = "Today you've spent %s" % utils.speakable_currency(res['spend_today'])
    return response.build("Spent Today", output)

def balance_request(access_token, account_id):
    params = {"account_id": account_id}
    res = api.request(api.BALANCE_URI, params, access_token)
    return res

