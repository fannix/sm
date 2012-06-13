"""Trading model
"""
import MySQLdb
from collections import defaultdict
import random
import numpy as np
from stock import Stock, Trade
import pandas
import datetime


class TradingModel:
    def __init__(self, company_id):
        self.company_id = company_id

    def load_emotion_serie(self, time_li, emotion_li):
        self.time_li = time_li
        self.emotion_li = emotion_li
        self.emotion_timeline = pandas.Series(emotion_li, time_li)

    def load_stock_market(self, stock, market):
        self.stock = stock
        self.market = market

    def trade_at(self, year, season):
        start_date_li = ['03-21', '06-21', '09-21', '12-21']
        end_date_li = ['03-31', '06-30', '09-30', '12-31']

        start_date = "%d-%s" % (year, start_date_li[season-1])
        end_date = "%d-%s" % (year, end_date_li[season-1])
        emotion_sum = sum(self.emotion_timeline[start_date: end_date])

        a_trade = Trade(self.stock, self.market)
        format = "%Y-%m-%d"
        start_datetime = datetime.datetime.strptime(start_date, format)
        end_datetime = datetime.datetime.strptime(end_date, format)
        trade_starttime = start_datetime + 1 * pandas.datetools.BDay()
        trade_endtime = end_datetime + 10 * pandas.datetools.BDay()

        trade_start = trade_starttime.strftime(format)
        trade_end = trade_endtime.strftime(format)
        print trade_start, trade_end
        try:
            if emotion_sum > 0.01:
                trade_result = a_trade.trade(100, trade_start, trade_end)
            elif emotion_sum < -0.01:
                trade_result = a_trade.trade(100, trade_end, trade_start)
            else:
                trade_result = 0
        except KeyError:
            print "Key error"
            trade_result = 0

        print trade_result
        return trade_result

    def trade(self):
        print "company_id", self.company_id
        profit = []

        profit.append(self.trade_at(2010, 4))
        profit.append(self.trade_at(2011, 1))
        profit.append(self.trade_at(2011, 2))
        profit.append(self.trade_at(2011, 3))

        print profit, sum(profit)
        return sum(profit)

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

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", # your host, usually localhost
            user="root", # your username
            passwd="", # your password
            db="test") # name of the data base
    cur = db.cursor()

    row_li = []

    period = [('2010-12-21', '2010-12-31'), ('2011-03-21', '2011-03-31'), ('2011-06-21', '2011-06-30'),
            ('2011-09-21', '2011-09-30'), ('2011-12-21', '2011-12-31')]
    stat_pat = "select compnay_id, created_at, emotion \
            from company_emotion where created_at between '%s' and '%s'"

    for (start, end) in period:
        cur.execute(stat_pat % (start, end))
        row_li.extend(cur.fetchall())
    # each row is a tuple of (long, datetime.datetime, float)
    #print row_li

    profit_bootstrap = []
    for i in range(2):
        company_sample_li = random.sample(xrange(3, 23), 3)

        stock_li, market = load_stock()

        profit = []
        for company_id in company_sample_li:
            time_li = [row[1] for row in row_li if row[0] == company_id]
            emotion_li = [row[2] for row in row_li if row[0] == company_id]
            stock  = [stock for stock  in stock_li if stock.company_id == company_id][0]

            #print time_li
            #print emotion_li

            model = TradingModel(company_id)
            model.load_emotion_serie(time_li, emotion_li)
            model.load_stock_market(stock, market)
            profit.append(model.trade())
            print
        profit_bootstrap.append(np.mean(profit))

    print profit_bootstrap
    print np.mean(profit_bootstrap), np.std(profit_bootstrap)

