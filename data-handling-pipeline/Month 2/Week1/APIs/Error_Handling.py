# Topic 7 — Error Handling and Rate Limiting
# Explanation
#
# When working with APIs, requests do not always succeed.
#
# Problems can happen such as:
# API server is down
# Wrong endpoint
# Network failure
# Invalid JSON response
# Too many requests
#
# If we do not handle these cases, the program may crash.
# Error handling ensures that the program fails safely and continues running.


# 1️⃣ Checking Status Codes (Basic Error Handling)
# Explanation
# Before using the API data, we should always verify that the request succeeded.
#
# The safest condition is:
# status_code == 200
#
# Meaning:
# Request succeeded

# Example
import requests
url = "https://api.coingecko.com/api/v3/coins/bitcoin"
response = requests.get(url)
if response.status_code == 200:
    data = response.json()
    print(data["name"])
else:
    print("Request failed:", response.status_code)

# Example output: Bitcoin
# If the request fails: Request failed: 404




# 2️⃣ Handling JSON Errors (try-except)

# Explanation
# Sometimes the API response may not contain valid JSON.
#
# Calling:
#     response.json()
#
# could cause an error.
# To prevent program crashes, we use try–except.

import requests
from json import JSONDecodeError

url = "https://api.coingecko.com/api/v3/coins/bitcoin"
response = requests.get(url)
try:
    data = response.json()
    print(data["name"])
except JSONDecodeError:
    print("Invalid JSON response")
# This ensures the program does not stop unexpectedly.




# 3️⃣ Rate Limiting

# Explanation
#
# Most APIs restrict how many requests you can send.
#
# Example limits:
# 50 requests per minute
# 100 requests per minute
#
# If you send too many requests quickly, the API returns:
# 429 Too Many Requests
#
# To avoid this, we add delay between requests.


# Example Using time.sleep()
import requests
import time
url = "https://api.coingecko.com/api/v3/coins/bitcoin"
for i in range(5):
    response = requests.get(url)
    print(response.status_code)

    time.sleep(1) # this adds delay ensuring no 429 error

# Meaning
# Wait 1 second before sending the next request

# Example Flow
# Send request
    # ↓
# Check status_code
    # ↓
# If success → parse JSON
# If failure → handle error
    # ↓
# Add delay between requests

# Real Data Collection Example
import requests
import time

url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd",
    "per_page": 3
}
for i in range(3):
    response = requests.get(url, params=params)
    if response.status_code == 200:
        data = response.json()

        for coin in data:
            print(coin["name"], coin["current_price"])

    time.sleep(1)


# Fix 2 — Handle 429 Properly (Best Practice)
# Real API pipelines detect 429 and wait.

import requests
import time

url = "https://api.coingecko.com/api/v3/coins/markets"

params = {
    "vs_currency": "usd",
    "per_page": 3
}

for i in range(3):

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()

        for coin in data:
            print(coin["name"], coin["current_price"])

    elif response.status_code == 429:
        print("Rate limit reached. Waiting...")
        time.sleep(30)

    else:
        print("Error:", response.status_code)

    time.sleep(5)

