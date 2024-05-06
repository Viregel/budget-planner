from datetime import date, timedelta, datetime

today = date.today()
this_month = today.strftime("%Y-%m")


def nDayRange(day, n=30):
    end = datetime(day.year, day.month, day.day)
    d = timedelta(days=n)
    start = end - d
    start = start.strftime("%Y-%m-%d")
    end = end.strftime("%Y-%m-%d")
    return start, end


def getMonthStartAndEnd(YM):
    year = YM.year
    month = YM.month
    # TODO: Convert to strptime
    start = date(year, month, 1)
    end = date(year, month+1, 1) + timedelta(days=-1)
    start = start.strftime("%Y-%m-%d")
    end = end.strftime("%Y-%m-%d")
    return start, end


def daysElapsedThisMonth(day=today):
    day = datetime(day.year, day.month, day.day)
    start = datetime.strptime(getMonthStartAndEnd(day)[0], '%Y-%m-%d')
    num_days = (day - start).days + 1
    return num_days


def daysRemainingThisMonth(day=today):
    day = datetime(day.year, day.month, day.day)
    end = datetime.strptime(getMonthStartAndEnd(day)[1], '%Y-%m-%d')
    num_days = (end - day).days + 1
    return num_days


daysElapsed = daysElapsedThisMonth()
daysRemaining = daysRemainingThisMonth()
