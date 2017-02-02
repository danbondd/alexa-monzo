import isodate

import api
import response
import utils

from datetime import datetime, timedelta

def get_transactions(access_token, account_id, slots):
    if "value" not in slots['duration']:
    	return response.error()

    category = None
    	
    if "value" in slots['category']:
    	category = slots['category']['value']

    duration = slots['duration']['value']
    td_duration = isodate.parse_duration(duration)
    now = datetime.utcnow()
    date = now - td_duration
    # TODO add timezone correctly
    date = "%sZ" % date.isoformat()

    url = "%s%s?account_id=%s&since=%s" % (api.BASE_URL, api.TRANSACTIONS_URI, account_id, date)
    if category is not None:
    	url = "%s&category=%s" % (url, category.replace(" ", "_"))

    res = api.do_request(url, access_token)
    
    if res == None:
	return response.error()

    total = 0
    for transaction in res['transactions']:
	if category is not None:
	    if transaction['category'] == category:
    	        total += transaction['amount']
	else:
	    total += transaction['amount']    	
    
    output = "In the last %s, you've spent %s" % (utils.duration_to_words(duration), utils.speakable_currency(total))
    if category is not None:
    	output = "%s on %s" % (output, category)
    return response.build("Get Transactions", output)
