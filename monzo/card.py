import api
import response

def get_status(access_token, account_id):
    url = "%s%s?account_id=%s" % (api.BASE_URL, api.CARD_LIST_URI, account_id)
    res = api.do_request(url, access_token)

    if res == None:
        return response.error()

    output = "Your Monzo card is currently %s" % res['cards'][0]['status']
    return response.build("Card Status", output)

