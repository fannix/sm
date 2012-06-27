"""Trading by comparing the price at the begin and end of a window period,
"""
from stock import Stock, Trade
import pandas
import datetime


class EndPointComparisonTradingModel:
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
        start_date_li = ['03-11', '06-11', '09-11', '12-11']
        end_date_li = ['03-31', '06-30', '09-30', '12-31']

        format = "%Y-%m-%d"
        start_date = datetime.datetime.strptime("%d-%s" % (year, start_date_li[season-1]), format)
        end_date = datetime.datetime.strptime("%d-%s" % (year, end_date_li[season-1]), format)
        emotion_timeline = self.emotion_timeline[start_date: end_date]
        print emotion_timeline
        timeline1 = emotion_timeline[:-1]
        timeline2 = emotion_timeline[1:]
        delta = timeline2.values - timeline1.values

        buy = sell = False
        print delta
        if emotion_timeline[-1] - emotion_timeline[0] > 0.01:
            buy = True
        elif emotion_timeline[-1] -  emotion_timeline[0] < -0.01:
            sell = True

        a_trade = Trade(self.stock, self.market)
        end_datetime = end_date
        trade_starttime = end_datetime + 30 * pandas.datetools.BDay()
        trade_endtime = end_datetime + 40 * pandas.datetools.BDay()

        trade_start = trade_starttime.strftime(format)
        trade_end = trade_endtime.strftime(format)
        print trade_start, trade_end
        try:
            if buy:
                print "buy",
                trade_result = a_trade.trade(100, trade_start, trade_end)
            elif sell:
                print "sell",
                trade_result = a_trade.trade(100, trade_end, trade_start)
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
