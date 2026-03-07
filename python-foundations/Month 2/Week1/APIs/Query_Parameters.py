# Topic 5 — Query Parameters (params)
# Explanation:
# Many APIs allow you to customize the data returned by sending query parameters.
# Query parameters are key–value pairs added to a URL to filter or control the request.

# Example API request:
# https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=1

# Here:
# vs_currency = usd
# days = 1
# These are parameters

# Meaning:
# Give Bitcoin market data
# Currency = USD
# For the last 1 day

# Structure of Query Parameters
#
# General format:
# base_url?key=value&key=value
#
# Example:
# https://api.example.com/data?country=india&year=2024
#
# Where:
# country = india
# year = 2024



# Using Parameters in Python
#
# Instead of manually writing them in the URL, we use a dictionary.
#
# params = {
#     "key": "value"
# }
# Then pass it to requests.get()


# Example 1 — Using CoinGecko API
# Goal:
# Get Bitcoin market data in USD for 1 day

import requests

url = "https://api.coingecko.com/api/v3/coins/bitcoin/market_chart"
params = {
    "vs_currency" : "usd",
    "days" : "1"
}
response = requests.get(url , params=params)
data = response.json()
print(data)

# Python automatically converts this to:
# https://api.coingecko.com/api/v3/coins/bitcoin/market_chart?vs_currency=usd&days=1


# Example 2 — Get Top Cryptocurrencies
# API:
# https://api.coingecko.com/api/v3/coins/markets

import requests

url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd",
    "per_page": 5,
    "page": 1
}

response = requests.get(url , params=params)
data = response.json()
for coin in data:
    print(coin["name"] , coin["current_price"])

# Example Flow
# Python program
      # ↓
# params dictionary
      # ↓
# requests.get(url, params=params)
      # ↓
# API server receives request
      # ↓
# API returns filtered data

# Why Parameters Are Important
#
# Without parameters:
# API may return huge data
#
# With parameters:
# You request only the data you need
