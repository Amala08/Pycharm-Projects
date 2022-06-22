import csv
import requests

response = requests.get("https://api.coingecko.com/api/v3/exchange_rates")
rate = response.json()["rates"].values()
rate_list = []
[rate_list.append(list(ele.values())) for ele in rate]
print(rate_list)

with open("rates.csv", "w", encoding="utf-8") as rates:
    write = csv.writer(rates)
    write.writerow(rate_list)
