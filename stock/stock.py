import requests
from bs4 import BeautifulSoup
import time

#ticker = 'BHEL' #Ticker
#exchange = 'NSE' #NSE, BOM


def getRealTimePrice(ticker :str, exchange : str):
  for i in range(1):
    url = f'https://www.google.com/finance/quote/{ticker}:{exchange}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    class1 = "YMlKec fxKbKc"
    price = float(soup.find(class_=class1).text.strip()[1:].replace(",",""))
    return price