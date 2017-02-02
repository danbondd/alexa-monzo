import api
import response


def get_status(access_token, account_id):
    res = card_request(access_token, account_id)
    if res is None:
        return response.error()

    output = "Your Monzo card is currently %s" % res['cards'][0]['status']
    return response.build("Card Status", output)


def block_card(access_token, account_id):
    res = card_request(access_token, account_id)
    if res is None:
        return response.error()

    params = {"card_id": res['cards'][0]['id'], "status": "INACTIVE"} 
    blocked = api.request(api.CARD_TOGGLE_URI, params, access_token, 'PUT')
    if blocked is None:
        return response.error()

    output = "Your Monzo card has been successfully blocked."
    return response.build("Block Card", output)


def card_request(access_token, account_id):
    params = {"account_id": account_id}
    res = api.request(api.CARD_LIST_URI, params, access_token)
    return res
