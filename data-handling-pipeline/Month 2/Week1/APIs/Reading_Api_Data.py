# Topic 4 — Reading API Data (response.json() and response.text)
# Explanation
#
# After sending a request and checking the status code, the next step is to read the data returned by the API.
# The API usually sends data in JSON format.
#
# JSON stands for:
# JavaScript Object Notation
#
# It is a structured format for representing data, similar to a Python dictionary.

# Example JSON:
# {
#     "name": "Bitcoin",
#     "symbol": "btc",
#     "price": 68000
# }
#
# To access this data in Python, we use:
# response.json()



# 1️⃣ response.json()
# Explanation
# response.json() converts the JSON response into Python objects.
#
# Depending on the API response, it can become:
# Python dictionary
# Python list
#
# This allows us to access individual values using keys

#Example
import requests

url = "https://api.coingecko.com/api/v3/coins/bitcoin"
response = requests.get(url)
data = response.json()
print(data)
# This prints a large dictionary containing Bitcoin information.

# Example — Access Specific Data
import requests
url = "https://api.coingecko.com/api/v3/coins/bitcoin"
response = requests.get(url)
data = response.json()
print(data["id"])
print(data["symbol"])
print(data["name"])

#Output
# bitcoin
# btc
# Bitcoin

# Example — Access Nested Data
# Many APIs return nested dictionaries.
#
# Example structure:
# {
#     "market_data":
#         {
#             "current_price":
#                 {
#                     "usd": 68000
#                 }
#         }
# }

price = data["market_data"]["current_price"]["usd"]
print(price)
# Output example:
# 67966


# 2️⃣ response.text
# Explanation:
# response.text returns the raw response as a string.
# This means it does not convert JSON into Python objects.
#
# Example output:
# "{'id':'bitcoin','symbol':'btc','name':'Bitcoin'}"
# So it is usually less useful for data processing.

import requests
url = "https://api.coingecko.com/api/v3/coins/bitcoin"
response = requests.get(url)
print(response.text[:200])
# Here we print only the first 200 characters because the response is very large.
#
# Difference Between .json() and .text
# Method	                    Output	                    Use Case
# response.json()	        Python dictionary/list	    Best for data processing
# response.text	            Raw string	              Used when response isn't JSON
#
# For data pipelines and ML work, you will almost always use:
# response.json()

# Mini Example
import requests
url = "https://randomuser.me/api/"
response = requests.get(url)
data = response.json()
print(type(data))
print(data["results"][0]["name"]["first"])
# Example output:
# John

