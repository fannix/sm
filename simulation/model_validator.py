""" Conduct bootstrapping to validate the trading model
"""
import random
import numpy as np
from stock import Stock, Trade
from util import load_stock, load_emotion_from_mysql
from trading import EmotionSumTradingModel
from trading2 import EndPointComparisonTradingModel


def testEmotionSumTradingModel():
    row_li = load_emotion_from_mysql()
    # each row is a tuple of (long, datetime.datetime, float)
    #print row_li

    profit_bootstrap = []
    for i in range(5):
        company_sample_li = random.sample(xrange(3, 23), 15)

        stock_li, market = load_stock()

        profit = []
        for company_id in company_sample_li:
            time_li = [row[1] for row in row_li if row[0] == company_id]
            emotion_li = [row[2] for row in row_li if row[0] == company_id]
            stock  = [stock for stock  in stock_li if stock.company_id == company_id][0]

            #print time_li
            #print emotion_li

            model = EmotionSumTradingModel(company_id)
            model.load_emotion_serie(time_li, emotion_li)
            model.load_stock_market(stock, market)
            trade_result = model.trade()
            profit.append(trade_result)
            print
        profit_bootstrap.append(np.sum(profit))

    print profit_bootstrap
    print np.mean(profit_bootstrap), np.std(profit_bootstrap)


def testEndPointComparisonTradingModel():
    row_li = load_emotion_from_mysql()
    # each row is a tuple of (long, datetime.datetime, float)
    #print row_li

    profit_bootstrap = []
    for i in range(5):
        company_sample_li = random.sample(xrange(3, 23), 15)

        stock_li, market = load_stock()

        profit = []
        for company_id in company_sample_li:
            time_li = [row[1] for row in row_li if row[0] == company_id]
            emotion_li = [row[2] for row in row_li if row[0] == company_id]
            stock  = [stock for stock  in stock_li if stock.company_id == company_id][0]

            #print time_li
            #print emotion_li

            model = EndPointComparisonTradingModel(company_id)
            model.load_emotion_serie(time_li, emotion_li)
            model.load_stock_market(stock, market)
            trade_result = model.trade()
            profit.append(trade_result)
            print
        profit_bootstrap.append(np.sum(profit))

    print profit_bootstrap
    print np.mean(profit_bootstrap), np.std(profit_bootstrap)


if __name__ == "__main__":
    testEmotionSumTradingModel()
    #testEndPointComparisonTradingModel()
