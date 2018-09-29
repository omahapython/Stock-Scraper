import requests
from decouple import config
from datetime import date


class StockPopulate(object):

    """
    Uses the Python 3 requests package to download historic stock data and populate a django database
    requires an api key from https://www.alphavantage.co/documentation/

    :param symbol: the stock ticker symbol.
    :arg api_key: your alphavantage api key.
    :arg base_endpoint: the base of the endpoint you want to send post requests to.

    Change the above arguments in your .env file.  
    
    """

    def __init__(self, symbol, api_key=config('API_KEY'), base_endpoint=config('URL_BASE')):

        self.symbol = symbol
        self.api_key = api_key
        self.base_endpoint = base_endpoint
        # self.date = date

    def get_all_data(self):
        """
        Retrieves all daily historic stock proce data from the alphavantage api.
        """

        _parameters = {
           'function': 'TIME_SERIES_DAILY',
           'symbol': self.symbol,
           'outputsize': 'full',
           'apikey': self.api_key, 
        }
        _url = 'https://www.alphavantage.co/query?'

        r = requests.get(_url, params=_parameters)

        if r.status_code == 200:
            return r.json()

        else:
            raise ConnectionError

    def get_daily_data(self, date):

        """
        Retrieves stock data for a specific date from the alphavantage stock api.
        :arg date: The date you wish to receive stock data as a string.

        example usage date = str(datetime.date.today())
        """

        _parameters = {
           'function': 'TIME_SERIES_DAILY',
           'symbol': self.symbol,
           'outputsize': 'compact',
           'apikey': self.api_key, 
        }

        _url = 'https://www.alphavantage.co/query?'

        r = requests.get(_url, params=_parameters)

        if r.status_code == 200:
            
            data = r.json()['Time Series (Daily)']

            if date in data:
                self.date = date
                return data[date]
            
            else:
                raise KeyError
        
        else:
            raise ConnectionError

    def normalize_all_data(self, request):
        """
        :arg request: use self.get_all_data()
        A generator function used to iterate through self.get_all data() and prepare that data for posting to our api.

        """
        
        for date, info in request['Time Series (Daily)'].items():
            self.date = date

            data =  {
                 'open': info.get('1. open'), 
                 'close': info.get('4. close'),
                 'high': info.get('2. high'),
                 'low': info.get('3. low'),
                 'volume': info.get('5. volume'),
                 'date': self.date,
                 'symbol': self.symbol,
                }

            yield data

    def post_all_data(self, data):

        """
        :arg data: The iterable, normalized data you wish to post to our api.

        example:
        stock = StockPopulate('GOOG')
        stock.post_all_data(stock.normalize_all_data(stock.get_all_data()))
        """

        for d in data:

            p = requests.post(self.base_endpoint + '/api/daily_prices/', data=d)

            print(p.status_code, p.text)

    def populate_updated_data(self, request):

        """
        use get_daily_data(str(date.today())) as request argument
        """

        data =  {
             'open': request['1. open'],
             'close': request['4. close'], 
             'high': request['2. high'],
             'low': request['3. low'],
             'volume': request['5. volume'],
             'date': self.date,
             'symbol': self.symbol,
        }

        p = requests.post(self.base_endpoint + '/api/daily_prices/', data=data)

        print(p.status_code, p.text)