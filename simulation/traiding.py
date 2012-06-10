"""Trading model
"""
import MySQLdb
from collections import defaultdict
import random


class TradingModel:
    def __init__(self, company_id):
        self.company_id = company_id

    def load_data(self, time_li, emotion_li):
        self.time_li = time_li
        self.emotion_li = emotion_li
        self.date2emotion = defaultdict(lambda: 0)
        for i, t in enumerate(time_li):
            date = "%s %s" % (t.year, t.month)
            self.date2emotion[date] += emotion_li[i]

    def decide(self):
        for date in self.date2emotion:
            if self.date2emotion[date] > 0.001:
                print "company", self.company_id, ":buy at the end of %s and sell before report release" % date
            if self.date2emotion[date] < -0.001:
                print "company", self.company_id, ":sell at the end of %s and buy before report release" % date

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", # your host, usually localhost
            user="root", # your username
            passwd="", # your password
            db="test") # name of the data base
    cur = db.cursor()

    row_li = []

    period = [('2010-12-21', '2010-12-31'), ('2011-3-21', '2011-3-31'), ('2011-6-21', '2011-6-30'),
            ('2011-9-21', '2011-9-30'), ('2011-12-21', '2011-12-31')]
    stat_pat = "select compnay_id, created_at, emotion \
            from company_emotion where created_at between '%s' and '%s'"

    for (start, end) in period:
        cur.execute(stat_pat % (start, end))
        row_li.extend(cur.fetchall())
    #print row_li

    company_sample_li = random.sample(xrange(3, 23), 15)

    for company_id in company_sample_li:
        time_li = [row[1] for row in row_li if row[0] == company_id]
        emotion_li = [row[2] for row in row_li if row[0] == company_id]

        #print time_li
        #print emotion_li

        model = TradingModel(company_id)
        model.load_data(time_li, emotion_li)
        model.decide()
        print
