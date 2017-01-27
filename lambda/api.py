import urllib2

BASE_URL = "https://api.monzo.com/"
BALANCE_URI = "balance"

def do_request(uri):
    req = urllib2.Request(BASE_URL)
    req.add_header("Authorization", "Bearer" + "")

