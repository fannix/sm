"""Simulation of stock trading operation
"""

class Stock:
    """ Stock object holds information about this stock
    """

    def __init__(self, company_id, company_name, date_list, price_list):
        self._company_id = company_id
        self._company_name = company_name
        self.date_list = date_list
        self.price_list = price_list
        self._date_to_price = {}

        for i, date in enumerate(self.date_list):
            self._date_to_price[date] = self.price_list[i]

    @property
    def company_id(self):
        return self._company_id

    @property
    def company_name(self):
        return self._company_name

    def price_at(self, date):
        return self._date_to_price[date]

class Trade:
    """Simulate trading behaviour
    """
    def __init__(self, stock_to_trade, market):
        self.stock_to_trade = stock_to_trade
        self.market = market

    def trade(self, number, buy_date, sell_date):
        """return profit by traiding number unit stock at buy_date and sell_date
        """
        spend = number * (self.stock_to_trade.price_at(buy_date) - self.market.price_at(buy_date))
        earn = number * (self.stock_to_trade.price_at(sell_date) - self.market.price_at(sell_date))
        return earn - spend

def test_stock():
    stock1 = Stock(20, "Example", ["2000-01-01", "2001-01-01"], [10, 20])
    assert stock1.company_id == 20
    assert stock1.company_name == "Example"

def test_trade():
    stock1 = Stock(1, "Ex1", ["2000-01-01", "2001-01-01"], [20, 30])
    market = Stock(0, "market", ["2000-01-01", "2001-01-01"], [10, 10])
    trade1 = Trade(stock1, market)
    assert trade1.trade(100, "2000-01-01", "2001-01-01") == 1000
