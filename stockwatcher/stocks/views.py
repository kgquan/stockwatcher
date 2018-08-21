from django.http import HttpResponse
from django.template import loader
from . import services
from django.http import Http404

def detail(request, symbol):
    """
    Stock detail view.
        :param request: The request
        :param symbol: The trading symbol or ticker, e.g. "AAPL" for Apple Inc.
    """
    template = loader.get_template('stocks/detail.html')

    stock_info_from_api = services.get_stock(symbol)

    if stock_info_from_api is None:
        raise Http404("Stock with symbol " + str(symbol) + " does not exist.")

    stock_quote = {
        'symbol': stock_info_from_api['quote']['symbol'],
        'company_name': stock_info_from_api['quote']['companyName'],
        'latest_price': stock_info_from_api['quote']['latestPrice'],
        'open': stock_info_from_api['quote']['open'],
        'close': stock_info_from_api['quote']['close'],
        'high': stock_info_from_api['quote']['high'],
        'low': stock_info_from_api['quote']['low']
    }

    return HttpResponse(template.render(stock_quote, request))

def index(request):
    """
    The stock index view.
        :param request: The request
    """
    template = loader.get_template('stocks/index.html')
    context = {}
    return HttpResponse(template.render(context, request))
