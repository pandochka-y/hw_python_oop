import datetime as dt

class Calculator:
    def __init__(self, limit):
        self.limit = limit
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        count_today = 0
        today = dt.datetime.now().date()
        for rec in self.records:
            if rec.date == today :
                count_today += rec.amount
        return count_today                    

    def get_week_stats(self):
        count_week = 0
        today = dt.datetime.now().date()
        week_day = dt.timedelta(days=7)
        for rec in self.records:
            if week_day >= rec.date <= today:
                count_week += rec.amount
        return count_week        





class Record(Calculator):
    def __init__(self, amount, comment, date=''):
        self.amount = amount
        self.comment = comment
        if date == '':
                self.date = dt.datetime.now().date()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y')       

class CashCalculator(Calculator):
    USD_RATE = 75
    RUB_RATE = 1
    EURO_RATE = 90

    currencies = {
            'usd': (USD_RATE, 'USD'),
            'euro': (EURO_RATE, 'EURO'),
            'rub': (RUB_RATE, 'руб'),
    }

    def get_today_cash_remained(self, currency):
        today_stats = self.get_today_stats
        limit = self.limit
        dict = CashCalculator.currencies
        for cur in dict:
            if cur == currency:
                for i in dict[cur].split():
                    count_cur = today_stats/dict[cur].split[1]

                    if count_cur < (limit/dict[cur].split[1]):
                        print(f'На сегодня осталось {count_cur} {dict[cur].split[2]}')

                    elif count < (limi)
        
#ыплит в словаре не работает, обдумать!!!!
        
    




class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        today_stats = self.get_today_stats
        limit = self.limit
        if today_stats < limit:
            stats = limit - today_stats
            print(f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {stats} кКал')
        elif today_stats >= limit:
            print('Хватит есть!')    


ref = CashCalculator.add_record(Record(1000, 'sss'))