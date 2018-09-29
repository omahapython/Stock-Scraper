# Introduction

This project aggregates historic stock data, relevant information, and news concerning specific publicly traded companies selected by the user.

The goal of this project is to provide the user with an automatically updating API containing only the data they care about.

# Quick Start

## The API
* Clone this repo in the directory you want to place it in.
* Create a new virtual environment and activate it.
* Run `pip install -r requirements.txt`.
* Rename the `model.env` file to `.env`
* Retrieve a free API key from https://www.alphavantage.co
* Place your API key after `API_KEY=` in your `.env` file DO NOT PLACE IT IN QUOTES.
* Alter the setting for `URL_BASE=` to `http://localhost:8000` in your `.env` file DO NOT PLACE IT IN QUOTES.
* Start the Django development server `python manage.py runserver`.
* Navigate to `http://localhost:8000/api/stocks_followed/` and add the ticker symbol of a stock you want data on.
* Manually (for now) run the update scripts, which are located in `popoulate.py` and enjoy.

# A Short Example

Lets say you want all the stock data on Google (GOOG).  After adding GOOG to `http://localhost:8000/api/stocks_followed/` do the following with your virtual environment activated.

## Adding All Data

``` python
>>> from populate import StockPopulate
>>> stock = StockPopulate('GOOG')

# Create a variable for your stock data
>>> data = stock.get_all_data()
# Normalizes, and creates an iterable of the data, to post to our API
>>> stream = stock.normalize_all_data(data)
# Post the data to our API
>>>stock.post_all_data(stream)

# Or if you prefer a one liner
 stock.post_all_data(stock.normalize_all_data(stock.get_all_data()))
```

## Updating Data With Specific Date

```python
>>> from populate import StockPopulate
>>> from datetime import date

>>> stock = StockPopulate('GOOG')
# TODO check to see if the market was active that day.
# Pass the date argument as a string 
date = str(date.today())
# or
date = '2018-09-28'
data = stock.get_daily_data(date)
# post the data
stock.populate_updated_data(data)
```