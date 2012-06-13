"""Very naive trading
"""
import numpy as np
from stock import Stock, Trade

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

def test_load_stock():
    stock_li, market = load_stock()
    assert stock_li[0].company_id == 3
    assert stock_li[-1].company_id == 22

def simple_trade():
    """Naive trading strategy

    Buy 100 unit per stock at 2011-09-01 and sell at 2011-09-30
    """
    #Loading information
    stock_li, market = load_stock()
    profit = []
    for a_stock in stock_li:
        #Initializing Trade class with the stock and the overall market
        a_trade = Trade(a_stock, market)
        # Calling trade() with argument buy_date and sell_date, the
        # return value is the profit for this trade
        profit.append(a_trade.trade(100, "2011-09-01", "2011-09-30"))

    #You can check that the result is 0, since we are actually doing nothing
    print profit, sum(profit)

if __name__ == "__main__":
    simple_trade()

