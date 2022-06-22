import csv
import requests


response = requests.get("https://api.coingecko.com/api/v3/exchange_rates")
rate = response.json()["rates"].values()
rate_list = []
[rate_list.append(list(ele.values())) for ele in rate]

with open("../pythonProject15/rates.csv","w") as rates:
    write = csv.writer(rates)
    


