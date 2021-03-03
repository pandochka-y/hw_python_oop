USD_RATE = 75
RUB_RATE = 1
EURO_RATE = 90

currencies = {
    'usd': (USD_RATE, 'USD'),
    'euro': (EURO_RATE, 'EURO'),
    'rub': (RUB_RATE, 'руб')
}


def test(cur):
    ttest = currencies[cur][0] * 2
    print(ttest)


test('usd')    
