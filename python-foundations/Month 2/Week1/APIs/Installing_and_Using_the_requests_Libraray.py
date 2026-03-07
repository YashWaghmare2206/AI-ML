# # Topic 2 — Installing and Using the `requests` Library (Your First API Request)
#
# ## Explanation
# To interact with APIs in Python, we use the **`requests` library**.
#
# `requests` is a Python library that allows us to **send HTTP requests** such as:
#
# GET
# POST
# PUT
# DELETE
# For **data collection in ML**, the most common request type is:
#
# ```
# GET
# `GET` is used to **retrieve data from an API endpoint**.
#
# The typical workflow is:
# Python code → requests.get() → API server → response object → data
# ```
# The API sends back a **response**, which Python stores in a **response object**.



# # Step 1 — Install the Library
#
# ## Explanation
# Before using `requests`, we need to install it.
# This is done using **pip**, Python’s package manager.
# ## Example
#
# ```python
# pip install requests # in terminal
# ```
#
# After installation, you can import it in Python.
# ```python
# import requests
# ```
#
# # Step 2 — Sending Your First API Request
#
# ## Explanation
# To fetch data from an API, we use:
# ```python
# requests.get(url)

# Where:
#
# url = API endpoint
# ```
# The function returns a **response object**, which contains:
#
# * status code
# * headers
# * response data
# * metadata
#

# ## Example
#
# ```python
# import requests
# url = "https://api.coingecko.com/api/v3/coins/bitcoin"
# response = requests.get(url)
# print(response)
# ```
# ### Output
# <Response [200]>
# ```

# # Understanding the Output
#
# <Response [200]>
# `200` means:
# Request was successful
# ```
#
# This means the API successfully returned the data.
#



# # Example 2 — Using Another API
#
# Let's fetch **random user data**.
#
# API:
# https://randomuser.me/api/
# ```
# Code:
# ```python
import requests
url = "https://randomuser.me/api/"
response = requests.get(url)
print(response)
# ```

# Output:
# <Response [200]>
# This means the API returned data successfully.



# # Example Flow
#
# Step 1
# Python sends request
# ↓
# requests.get(url)
#
# Step 2
# API processes request
# ↓
#
# Step 3
# API sends response
# ↓
#
# Step 4
# Python receives response object
# ```
#
# ---
#
# # Key Concept From This Topic
#
# You now know how to:
#
# ```
# Install requests
# Import requests
# Send GET request to API
# Receive response object
# ```
#
# This is the **first step of any API data pipeline**.
