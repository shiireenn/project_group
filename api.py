# Import Path function from pathlib
from pathlib import Path
# Import json
import json
# Import re
import re
# Import requests
import requests

# Instantiate summary_path to summary_report.txt
summary_path = Path.cwd()/"summary_report.txt"

# Create a function named api_function
def api_function():
    """
    - This function will retrieve the currency exchange rate of USD and SGD
    - This function will convert the amount of money from USD to SGD
    """
    # Assign the API URL to url
    url = "https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=USD&to_currency=SGD&apikey=OX96WV3X7K2KBVZ5"
    # Use .get() to request access
    response = requests.get(url)
    # Use .json() retreive data from .json from response
    data = response.json()
    # Use .dumps() convert into json string
    data = json.dumps(data, indent = 4)
    # Use re.search() to search for Exchange Rate:
    data = re.search(pattern = 'Exchange Rate": ".+', string = data).group()
    # Change varible data to forex and convert to float
    forex = float(data.replace('Exchange Rate": "','').strip('",'))
    # Open summary_path and append
    with summary_path.open(mode = "a", encoding = "UTF-8", newline = "") as file:
        # Use .write() to write the data into summary_path
        file.write("[REAL TIME CURRENCY CONVERSION RATE] " + "USD1 = SGD" + str(forex))
    # Returns the foreign exchange of USD to SGD
    return forex
   