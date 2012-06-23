from datetime import date, timedelta

class TradingModel:

    def set_trading_window_model(self, twm):
        self.traiding_window_model = twm

    def trade_at(self):
        start_date, end_date = self.traidng_window_model.get_window()

class TradingWindowModel:
    """Base class of obtain trading window
    """

    def get_window(self):
        pass


class FixDayModel(TradingWindowModel):
    """
    This simple model use fix days as trading window
    """

    def __init__(self, year, season, start_day=1, window=31):
        self.year = year
        self.season = season
        self.start_day =  start_day
        self.window = window

    def get_window(self):
        season_start_month = [1, 4, 7, 10]
        month = season_start_month[self.season-1]
        start_date = date(self.year, month, self.start_day)
        date_delta = timedelta(days=self.window)
        end_date = start_date + date_delta
        day_str1 = start_date.strftime("%Y-%m-%d")
        day_str2 = end_date.strftime("%Y-%m-%d")
        return day_str1, day_str2

class ReleaseDayModel(TradingWindowModel):
    """
    This model compute window around the earnings report release date
    """

    def __init__(self, before_days, after_days):
        """before_days: days before the earning report
        after_days: days after the earning report
        """

    def get_window(self):
        pass

    def set_release_day(self, release_day):
        self.release_day = release_day

    def set_emotion_series(self, li):
        pass

    def set_price_series(self, li):
        pass


def testFixDayModel():
    fdm = FixDayModel(2001, 1)
    start_day, end_day = fdm.get_window()
    assert start_day == "2001-01-01"
    assert end_day == "2001-02-01"

def testReleaseDayModel():
    pass

if __name__ == "__main__":
    testFixDayModel()
    #model = TradingModel()

    #report_ts = []
    #twm = TradingWindowModel(report_series)
    #model.set_trading_window_model(twm)
