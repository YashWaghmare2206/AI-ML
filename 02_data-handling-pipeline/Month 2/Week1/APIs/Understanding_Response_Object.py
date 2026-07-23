# When you send a request using:
#
# response = requests.get(url)
# Python does not directly give you the data.
# Instead, it returns a Response Object.
#
# This object contains all information about the API response, such as:
# status code
# headers
# response data
# metadata
# You must first check if the request was successful before using the data.


# Important Attributes of Response Object
# 1️⃣ response.status_code
# Explanation:
# status_code tells us whether the request succeeded or failed.
# It is an HTTP status code returned by the server.

# Example codes:

# Code	Meaning
# 200	Request successful
# 201	Created successfully
# 400	Bad request
# 401	Unauthorized
# 404	Resource not found
# 500	Server error
# Example

import requests
url = "https://api.coingecko.com/api/v3/coins/bitcoin"
response = requests.get(url)
print(response.status_code)

# Output:
# 200
# Meaning:
# The API request succeeded

import requests
url = "https://api.coingecko.com/api/v3/coins/bitcoin123"
response = requests.get(url)
print(response.status_code)

# Output:
# 404
# Meaning:
# The endpoint does not exist

# 2️⃣ response.ok
# Explanation
# response.ok is a boolean value that tells if the request succeeded.
#
# Rule:
# status_code < 400 → True
# status_code ≥ 400 → False

import requests
url = "https://api.coingecko.com/api/v3/coins/bitcoin"
response = requests.get(url)
print(response.ok)
# Output:
# True

# Example With Error
import requests
url = "https://api.coingecko.com/api/v3/coins/bitcoin123"
response = requests.get(url)
print(response.ok)
# Output:
# False



# 3️⃣ Checking Before Using Data (Important Practice)

import requests
url = "https://api.coingecko.com/api/v3/coins/bitcoin"
response = requests.get(url)
if response.status_code == 200:
    print("Request successful")
else:
    print("Request failed")
# This prevents your program from crashing when API fails.

# Flow

# requests.get(url)
# ↓
# response object
# ↓
# check status_code
# ↓
# if success → process data
# if fail → handle error



