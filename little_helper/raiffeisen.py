from bs4 import BeautifulSoup as bs
import requests


r = requests.get('https://www.raiffeisen.ru/currency_rates/?active_tab=offices')
html = bs(r.content, 'html.parser')

# for i in html.select('.b-table__row'):
#     if i.select('.desktop')[1].text == 'Доллар США':
#         for q in i.select('.desktop')[1].text == 'Доллар США':

# qwe = html.find("div", {"id": "offices"})
# ewq = qwe.select('.b-table__row')[0]
dollar_buy = html.find("div", {"id": "offices"}).select('.b-table__row')[0].select('.b-table__td')[3].text
dollar_sell = html.find("div", {"id": "offices"}).select('.b-table__row')[0].select('.b-table__td')[5].text
print(dollar_buy, dollar_sell)