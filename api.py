from pathlib import Path
import requests
import json,re

summary_path = Path.cwd()/"csv_reports"/"summary_report.txt"

# Create api_function
def api_function():
    url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=OX96WV3X7K2KBVZ5"
    response = requests.get(url)
    data = response.json()
    data = json.dumps(data, indent = 4)
    data = re.search(pattern = 'Exchange Rate": ".+', string = data).group()
    forex = float(data.replace('Exchange Rate": "','').strip('",'))
    with summary_path.open(mode = "a", encoding = "UTF-8", newline = "") as file:
        file.write("[REAL TIME CURRENCY CONVERSION RATE] " + "USD1 = SGD" + str(forex))
    return forex
   