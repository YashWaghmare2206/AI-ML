# Topic 6 — Headers (Sending Additional Information with Requests)
# Explanation
#
# When sending an API request, sometimes the server requires additional information about the request.]
# This information is sent through headers.
# Headers are key–value pairs that provide metadata about the request.
#
# They are commonly used for:
# identifying the client
# authentication
# content type
# security

# What Headers Look Like
#
# Example request headers:
# User-Agent: Mozilla/5.0
# Content-Type: application/json
# Authorization: Bearer API_KEY
#
# Meaning:
#
#     Header	                                Purpose
#     User-Agent	                Identifies the program sending the request
#     Content-Type	                Format of the data being sent
#     Authorization	                Used for API authentication

# Why Headers Are Used:
# Some APIs block requests that do not include headers.
# For example, if the API thinks the request is from a bot or script, it may reject it.
# Adding headers helps make the request look like it came from a normal browser or authorized client.

# 1️⃣
# Creating Headers in Python
# Headers are written as a dictionary.
#
# Example:
# headers = {
#     "User-Agent": "Mozilla/5.0"
# }

# Example 1 — Simple Header
import requests

url = "https://api.coingecko.com/api/v3/coins/bitcoin"
headers = {
    "User-Agent": "Mozilla/5.0"
}
response = requests.get(url, headers=headers)
data = response.json()
print(data["name"])

# Example 2 — Using Headers with Parameters
import requests

url = "https://api.coingecko.com/api/v3/coins/markets"
params = {
    "vs_currency": "usd",
    "per_page": 3
}
headers = {
    "User-Agent": "Mozilla/5.0"
}
response = requests.get(url, params=params, headers=headers)
data = response.json()
for coin in data:
    print(coin["name"], coin["current_price"])


# When Headers Are Important
#
# You will definitely use headers when working with:
#
# OpenAI API
# Twitter API
# Google APIs
# Financial APIs
# Weather APIs
#
# Many APIs require authentication headers.
# Example:
# Authorization: Bearer YOUR_API_KEY


# Key Takeaways
#
# You now know how to:
# Create headers dictionary
# Send headers in requests.get()
# Combine headers and params
# Understand why APIs require headers
