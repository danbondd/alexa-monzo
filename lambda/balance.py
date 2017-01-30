import api
import helpers
import monzo 

def get_balance(access_token, account_id):
    res = balance_request(access_token, account_id)
    if res == None:
        return monzo.error_response()

    output = "Your balance is %s" % helpers.speakable_currency(res['balance'])
    return monzo.build_response("Get Balance", output)

def get_spend_today(access_token, account_id):
    res = balance_request(access_token, account_id)
    if res == None:
        return monzo.error_response()

    output = "Today you've spent %s" % helpers.speakable_currency(res['spend_today'])
    return monzo.build_response("Spent Today", output)

def balance_request(access_token, account_id):
    url = "%s%s?account_id=%s" % (api.BASE_URL, api.BALANCE_URI, account_id)
    res = api.do_request(url, access_token)
    return res

