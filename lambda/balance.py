import api
import helpers
import monzo 

def get_balance(access_token, account_id):
    url = "%s%s?account_id=%s" % (api.BASE_URL, api.BALANCE_URI, account_id)
    res = api.do_request(url, access_token)
    
    if res == None:
        return monzo.error_response()

    output = "Your balance is %s" % helpers.speakable_currency(res['balance'])
    return monzo.build_response("Monzo - Get Balance", output)
