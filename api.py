import requests
from bs4 import BeautifulSoup
import re
from threading import Thread

def all_available_currencies():
    url = "https://wise.com/us/currency-converter/currencies"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")
    print(soup)
    vals = soup.find_all(class_ = "_currencyCard__currencyCode_angxx_1")
    currencies = []

    for i in range(len(vals)):
          val = vals[i]
          currency = re.match("<[^>]+>(.*)<[^>]+>", str(val)).group(1)
          currencies.append(currency)
    return currencies


def find_conversion_rate(currency_from, currency_to):
	url = "https://transferwise.com/us/currency-converter/" + currency_from + "-to-" + currency_to + "-rate?amount=1"
	response = requests.get(url)
	soup = BeautifulSoup(response.text, "html.parser")
	conversion_rate = float(soup.find(class_ = "text-success").get_text().replace(',', ''))
	return conversion_rate


currencies = all_available_currencies()
print(currencies)
conversion_table = [[0.0 for _ in range(len(currencies))] for _ in range(len(currencies))]
print(conversion_table)
def find_all_exchange_rates(conversion_table):
    # Finding all exchange rates
    for f in range(len(currencies)):
        for t in range(f, len(currencies)):
            f_currency = currencies[f]
            t_currency = currencies[t]
            print(f_currency, t_currency)
            if (f_currency == t_currency):
                conversion_table[f][t] == 1.0
            else:
                rate = find_conversion_rate(f_currency, t_currency)
                conversion_table[f][t] = rate
                conversion_table[t][f] = rate

thread = Thread(target = find_all_exchange_rates, args = (conversion_table, ) )
thread.start()
thread.join()
print(conversion_table)