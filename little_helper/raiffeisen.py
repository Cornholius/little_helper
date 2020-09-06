from bs4 import BeautifulSoup as bs
import requests


r = requests.get('https://www.raiffeisen.ru/currency_rates/?active_tab=offices')
html = bs(r.content, 'html.parser')

# for i in html.select('.b-table__row'):
#     if i.select('.desktop')[1].text == 'Доллар США':
#         for q in i.select('.desktop')[1].text == 'Доллар США':

# qwe = html.find("div", {"id": "offices"})
# ewq = qwe.select('.b-table__row')[0]
places = ["offices"]
price = []
for i in places:
    dollar_buy = html.find("div", {"id": i}).select('.b-table__row')[0].select('.b-table__td')[3].text
    dollar_sell = html.find("div", {"id": i}).select('.b-table__row')[0].select('.b-table__td')[5].text
    euro_buy = html.find("div", {"id": i}).select('.b-table__row')[1].select('.b-table__td')[3].text
    euro_sell = html.find("div", {"id": i}).select('.b-table__row')[1].select('.b-table__td')[5].text
    data = {'dollar_buy': dollar_buy,
            'dollar_sell': dollar_sell,
            'euro_buy': euro_buy,
            'euro_sell': euro_sell}
    price.append(i)
print(price)