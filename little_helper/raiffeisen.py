from bs4 import BeautifulSoup
import requests


class Raiffeisen:

    def __init__(self):
        self.r = requests.get('https://www.raiffeisen.ru/currency_rates/?active_tab=offices')
        self.html = BeautifulSoup(self.r.content, 'html.parser')
        self.data = {'id_offices': 'offices', 'id_online': 'online', 'id_card': 'card',
                     'us_str': 0, 'euro_str': 1,
                     'offices_buy_value': 3, 'offices_sell_value': 5,
                     'online_buy_value': 3, 'online_sell_value': 4,
                     'card_buy_value': 1, 'card_sell_value': 2}

    def getprice(self, ids, us_str, euro_str, buy_value, sell_value):
        usd = self.html.find("div", {"id": ids}).select('.b-table__row')[us_str]
        euro = self.html.find("div", {"id": ids}).select('.b-table__row')[euro_str]
        dollar_buy = usd.select('.b-table__td')[buy_value].text
        dollar_sell = usd.select('.b-table__td')[sell_value].text
        euro_buy = euro.select('.b-table__td')[buy_value].text
        euro_sell = euro.select('.b-table__td')[sell_value].text
        prices = {'dollar_buy': str(dollar_buy).replace(' ','').replace('\n', ''),
                  'dollar_sell': str(dollar_sell).replace(' ','').replace('\n', ''),
                  'euro_buy': str(euro_buy).replace(' ','').replace('\n', ''),
                  'euro_sell': str(euro_sell).replace(' ','').replace('\n', '')}
        return prices

    def office(self):
        return self.getprice(self.data['id_offices'], self.data['us_str'], self.data['euro_str'],
                             self.data['offices_buy_value'], self.data['offices_sell_value'])

    def online(self):
        return self.getprice(self.data['id_online'], self.data['us_str'], self.data['euro_str'],
                             self.data['online_buy_value'], self.data['online_sell_value'])

    def card(self):
        return self.getprice(self.data['id_card'], self.data['us_str'], self.data['euro_str'],
                             self.data['card_buy_value'], self.data['card_sell_value'])


qwe = Raiffeisen()
print(qwe.card())