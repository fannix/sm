"""Trading by inspecting the sum of emotion inside a window period,
"""

from collections import defaultdict
import random
import numpy as np
from stock import Stock, Trade
import pandas
import datetime
from util import load_stock, load_emotion_from_mysql


class EmotionSumTradingModel:
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

        format = "%Y-%m-%d"
        start_date = datetime.datetime.strptime("%d-%s" % (year, start_date_li[season-1]), format)
        end_date = datetime.datetime.strptime("%d-%s" % (year, end_date_li[season-1]), format)
        emotion_sum = sum(self.emotion_timeline[start_date: end_date])

        a_trade = Trade(self.stock, self.market)
        end_datetime = end_date
        trade_starttime = end_datetime + 20 * pandas.datetools.BDay()
        trade_endtime = end_datetime + 40 * pandas.datetools.BDay()

        trade_start = trade_starttime.strftime(format)
        trade_end = trade_endtime.strftime(format)
        print trade_start, trade_end
        money = 20000
        try:
            if emotion_sum > 0.01:
                print "buy",
                trade_result = a_trade.trade(money, trade_start, trade_end, False)
            elif emotion_sum < -0.01:
                print "sell",
                trade_result = a_trade.trade(money, trade_end, trade_start, False)
            else:
                print "skip",
                trade_result = 0
        except KeyError:
            print "Key error",
            trade_result = 0

        print trade_result
        return trade_result

    def trade(self):
        print "company_id", self.company_id
        profit = []

        trade_sequence = [(2010, 4), (2011, 1), (2011, 2), (2011, 3)]

        for e in trade_sequence:
            year, season = e
            trade_result = self.trade_at(year, season)
            profit.append(trade_result)
            if trade_result < 0:
                break

        print profit, sum(profit)
        return sum(profit)
