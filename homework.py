import datetime as dt


 #date_format = '%d.%m.%Y'

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
        week_ago = dt.datetime.now().date() - dt.timedelta(days=7)
        for rec in self.records:
            if rec.date > week_ago:
                count_week += rec.amount
        return count_week



class Record:
    def __init__(self, amount, comment, date=""):
        self.amount = amount
        self.comment = comment
        if date == "":
            self.date = dt.datetime.now().date()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()


class CashCalculator(Calculator):
    USD_RATE = 75.12
    RUB_RATE = 1.00
    EURO_RATE = 90.21

    currencies = {
        'usd': (USD_RATE, 'USD'),
        'eur': (EURO_RATE, 'EURO'),
        'rub': (RUB_RATE, 'руб')
    }

    def get_today_cash_remained(self, currency):
        dict_cur = self.currencies
        today_stats = self.get_today_stats()
        for cur in self.currencies:
            if cur == currency:
                limit = self.limit / dict_cur[cur][0]
                today_stats_rate = (today_stats / dict_cur[cur][0])
                current_cur = dict_cur[cur][1]
                if today_stats_rate > limit:
                    count_loan = today_stats_rate - limit
                    return f'Денег нет, держись: твой долг - {round((count_loan), 2)} {current_cur}'

                elif today_stats_rate == limit:
                    return 'Денег нет, держись'

                elif today_stats_rate < limit:
                    count = limit - today_stats_rate
                    return f'На сегодня осталось {round((count), 2)} {current_cur}'

            # elif cur != currency:
            #     return 'Денег нет, держись'

            # else:
            #     return 'Ошибка, неправильно введена валюта!'


class CaloriesCalculator(Calculator):
    def get_calories_remained(self):
        today_stats = self.get_today_stats()
        limit = self.limit
        stats = limit - today_stats
        if today_stats < limit:

            return f'Сегодня можно съесть что-нибудь ещё, но с общей калорийностью не более {stats} кКал'
        elif today_stats >= limit:
            return 'Хватит есть!'



cash_calculator = CashCalculator(1000)
        
# дата в параметрах не указана, 
# так что по умолчанию к записи должна автоматически добавиться сегодняшняя дата
cash_calculator.add_record(Record(amount=145, comment="кофе")) 
# и к этой записи тоже дата должна добавиться автоматически
cash_calculator.add_record(Record(amount=300, comment="Серёге за обед"))
# а тут пользователь указал дату, сохраняем её
cash_calculator.add_record(Record(amount=3000, comment="бар в Танин др", date="08.11.2019"))
                
print(cash_calculator.get_today_cash_remained('eur'))




# today_stats = self.get_today_stats() / dict_cur[currency][0]
        # limit = self.limit / dict_cur[currency][0]
        # res_limit = limit - today_stats
        # debt = today_stats - limit
        # if today_stats > limit:
        #     print(f'Денег нет, держись: твой долг {debt} {dict_cur[currency][1]}')
        #
        # elif today_stats == limit:
        #     print('Денег нет, держись')
        #
        # elif today_stats < limit:
        #     print(f'На сегодня осталось {res_limit} {dict_cur[currency][1]}')
        #
        # else:
        #     print('Ошибка, неправильно введена валюта!')