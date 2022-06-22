"""Using random module nd getting the random country nd their respective value from api file"""

import requests
import random
response = requests.get("https://api.coingecko.com/api/v3/exchange_rates")
country_rate = random.choice(list(response.json()["rates"].values()))
print(f"Currency Value of the {country_rate['name']} is {country_rate['value']}")



