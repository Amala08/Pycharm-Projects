""" Convert the rate api file to sqlite db file , find the max and min rate nd their respective country name """

import sqlite3
import requests
response = requests.get("https://api.coingecko.com/api/v3/exchange_rates")
rate = response.json()["rates"].values()
rate_list = []

[rate_list.append(list(ele.values())) for ele in rate]

connection = sqlite3.connect("rates.db")  # create a connection
cursor = connection.cursor()  # create a cursor
# cursor.execute("""CREATE TABLE money_rates(
#     name text,
#     unit txt,
#     value real,
#     crypto text
# )""")#create Table
# cursor.executemany("INSERT INTO money_rates VALUES (?, ?, ?, ?)", rate_list)
cursor.execute("SELECT name,value FROM money_rates WHERE value = (SELECT MAX(value) FROM money_rates)")
print(f"maximum  : {cursor.fetchall()}")
cursor.execute("SELECT name,value FROM money_rates WHERE value = (SELECT MIN(value) FROM money_rates)")
print(f"minimum  : {cursor.fetchall()}")
connection.commit()#commit the table
connection.close()

