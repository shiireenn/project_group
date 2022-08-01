from pathlib import Path
import requests
import json,re

url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=OX96WV3X7K2KBVZ5"

r = requests.get(url)
data = r.json()

print(data)