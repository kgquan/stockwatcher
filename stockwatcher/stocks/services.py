import requests
import django.core.exceptions
import urllib3.exceptions
import json

def get_stock(symbol):
    """
    Fetches stock information from the IEX API.
        :param symbol: The trading symbol or ticker, e.g. "AAPL" for Apple Inc.
    """

    url = 'https://api.iextrading.com/1.0/stock/' + symbol + '/batch'
    print(url)
    params = { 'types': 'quote' }

    try:
        req = requests.get(url, params=params)
        print(req.text)
        stock = req.json()

        stock_quote = {'quote': stock['quote']}
        return stock_quote

    except requests.exceptions.RequestException as re:
        print('%s (%s)' % (re.strerror, type(re)))

    except json.decoder.JSONDecodeError as jde:
        print('%s (%s)' % (jde.msg, type(jde)))

