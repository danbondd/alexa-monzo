import json
import urllib3

from urllib import urlencode

BASE_URL = "https://api.monzo.com/"
BALANCE_URI = "balance"
TRANSACTIONS_URI = "transactions"
CARD_LIST_URI = "card/list"
CARD_TOGGLE_URI = "card/toggle"


def request(uri, params, access_token, method='GET'):
    headers = {"Authorization": "Bearer %s" % access_token}
    
    urllib3.disable_warnings()
    http = urllib3.PoolManager()
    
    if method == 'PUT':
        uri += "?%s" % urlencode(params)
        params = None

    try:
        r = http.request(method, "%s%s" % (BASE_URL, uri), fields=params, headers=headers)
    except Exception as e:
        print e
        return None

    if r.status is not 200:
        print "Invalid status code: %s" % r.status
        return None

    return json.loads(r.data)
