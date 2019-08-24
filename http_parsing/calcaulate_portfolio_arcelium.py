import json
import requests
HOLDING_SERVICE_URL = "https://api.myjson.com/bins/1eleys"
PRICING_SERVICE_URL = "https://api.myjson.com/bins/vf9ac"

def fetch_security_holding(input_date):
    headers = {
        'Host': "api.myjson.com",
        }

    response = requests.request("GET", HOLDING_SERVICE_URL, headers=headers)
    return list(filter(lambda item: item['date'] == input_date , response.json()['data']))

def fetch_security_price(input_date):
    headers = {
        'Host': "api.myjson.com",
        }

    response = requests.request("GET", PRICING_SERVICE_URL, headers=headers)
    return list(filter(lambda item: item['date'] == input_date , response.json()['data']))

def calculateHoldingValue(date):
    quantities =  fetch_security_holding(date)
    prices = fetch_security_price(date)
    if len(quantities) == 0 or len(prices) == 0:
        return 0
        
    ticker_dict = {quantity['security']:[quantity['quantity']] for quantity in quantities}
    for price in prices:
        ticker_dict[price['security']].append(price['price'])

    total = 0
    for ticker in ticker_dict:
        if len(ticker_dict[ticker]) == 2:
            quantity = ticker_dict[ticker][0]
            price = ticker_dict[ticker][1]
            total += quantity*price
    return total

result = calculateHoldingValue('20190509')
print(result)
