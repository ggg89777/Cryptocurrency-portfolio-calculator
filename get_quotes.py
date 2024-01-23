import json

from requests import Session


def getinfo(tags: str, apy_key: str) -> json:  # Function to get the info

    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'  # Coinmarketcap API url

    parameters = {'symbol': tags,
                  'convert': 'USD'}  # API parameters to pass in for retrieving specific cryptocurrency data

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': apy_key
    }  # Replace 'YOUR_API_KEY'

    session = Session()
    session.headers.update(headers)
    response = session.get(url, params=parameters)
    return json.loads(response.text)

def get_price(json_resp, tag: str) -> float:
    return json_resp['data'][tag]['quote']['USD']['price']

def generate_dict_price(tags: str, apy_key: str) -> dict:
    list_price = []
    list_tag = []
    json_quotes = getinfo(tags=tags, apy_key=apy_key)

    for tag in tags.split(sep=','):
        price = get_price(json_resp=json_quotes, tag=tag)
        list_price.append(price)
        list_tag.append(tag)

    return {list_tag[i]: list_price[i] for i in range(0, len(list_tag), 1)}
