import json
import urllib2

BASE_URL = "https://api.monzo.com/"
BALANCE_URI = "balance"

def do_request(uri, access_token):
    req = urllib2.Request(uri)
    req.add_header("Authorization", "Bearer %s" % access_token)

    try:
        res = urllib2.urlopen(req)
        data = res.read()
        res.close()
    except urllib2.HTTPError as e:  
        print "Invalid HTTP response code: %s" % e.code
        return None
    except urllib2.URLError as e:
        print "Error performing request: %s" % e
        return None
    else:
        return json.loads(data)

