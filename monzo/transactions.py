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
    date = "%sZ" % date.isoformat()

    params = {"account_id": account_id, "since": date}
    if category is not None:
        params['category'] = category.replace(" ", "_")

    res = api.request(api.TRANSACTIONS_URI, params, access_token)
    if res is None:
        print("error getting transactions")
        return response.error()

    total = utils.calculate_total(res['transactions'], category)

    output = "In the last %s, you've spent %s" % (
        utils.duration_to_words(duration), utils.speakable_currency(total))

    if category is not None:
        output = "%s on %s" % (output, category)

    return response.build("Get Transactions", output)
