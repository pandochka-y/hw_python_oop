import datetime as dt


# date_format = '%d.%m.%Y'

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
            if rec.date == today:
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

    def showStat(self):
        return self.records


class Record:
    def __init__(self, amount, comment, date=""):
        self.amount = amount
        self.comment = comment
        if date == "":
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
                limit_rate = limit / dict[cur][0]
                today_stats_rate = today_stats / dict[cur][0]
                current_cur = dict[cur][1]
                if today_stats_rate > limit_rate:
                    count_loan = today_stats_rate - limit_rate
                    print(f'Денег нет, держись: твой долг {count_loan} {current_cur}')

                if today_stats_rate == limit_rate:
                    print('Денег нет, держись')

                if today_stats_rate < limit_rate:
                    count = limit_rate - today_stats_rate
                    print(f'На сегодня осталось {count} {current_cur}')

            else:
                print('Ошибка, неправильно введена валюта!')


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        today_stats = self.get_today_stats
        limit = self.limit
        if today_stats < limit:
            stats = limit - today_stats
            print(f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {stats} кКал')
        elif today_stats >= limit:
            print('Хватит есть!')
