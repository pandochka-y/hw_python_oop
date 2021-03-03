USD_RATE = 75
RUB_RATE = 1
EURO_RATE = 90

currencies = {
            'usd': (USD_RATE, 'USD'),
            'euro': (EURO_RATE, 'EURO'),
            'rub': (RUB_RATE, 'руб'),
    }


def get_today_cash_remained(currency):

        for cur in currencies:
            if cur == currency:
                for i in currencies[currencies[cur]].split(''):
                    count_cur = 1000/currencies[currencies[cur]].split()[1]

                    if count_cur < 100:
                        print(f'На сегодня осталось {1000} {currencies[currencies[cur]].split()[2]}')

                    


get_today_cash_remained('usd')                    