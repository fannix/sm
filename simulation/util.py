"""This module provide handy utilities
"""

import MySQLdb
from scipy import stats
from stock import Stock, Trade
import numpy as np

def slope(X, y):
    """Return the slope of regression line across [X, y]
    """

    slope, intercept, r_value, p_value, std_err = stats.linregress(X, y)

    return slope, r_value

def load_emotion_from_mysql():
    db = MySQLdb.connect(host="localhost", # your host, usually localhost
            user="root", # your username
            passwd="", # your password
            db="test") # name of the data base
    cur = db.cursor()

    stat_pat = "select compnay_id, created_at, emotion \
            from company_emotion"

    cur.execute(stat_pat)
    row_li = cur.fetchall()
    db.close()

    return row_li

def load_stock():
    """Load stock and market information
    """
    stock_array = np.loadtxt("company_finance.tsv", skiprows=1,
            dtype={'names': ('id', 'date', 'price'), 'formats': ('i8', 'S10', 'float')})
    market_array = np.loadtxt("market.tsv", skiprows=1,
            dtype={'names': ('date', 'total', 'price'), 'formats': ('S10', 'i8', 'float')})

    market = Stock(0, "market", list(market_array['date']), list(market_array['price']))
    stock_li = []

    stock_id_li = sorted(list(np.unique(stock_array["id"])))
    for stock_id in stock_id_li:
        stock_date = stock_array[stock_array["id"] == stock_id]["date"]
        stock_price = stock_array[stock_array["id"] == stock_id]["price"]
        stock_li.append(Stock(stock_id, str(stock_id), stock_date, stock_price))

    return stock_li, market
