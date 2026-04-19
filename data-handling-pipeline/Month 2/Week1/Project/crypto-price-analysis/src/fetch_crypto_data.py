import time

import pandas as pd
import requests
from json import JSONDecodeError

from pandas import Flags

coin_to_fetch = ["bitcoin", "ethereum", "solana", "cardano"]
coins_data = []
params = {
    "vs_currency":"usd",
    "days":30
}

header = {
    "User-Agent":"Mozilla/5.0"
}

try:

    for coin in coin_to_fetch:

        url = f"https://api.coingecko.com/api/v3/coins/{coin}/market_chart"

        response = requests.get(url, headers=header, params=params)
        temp_list = []

        if response.status_code == 200:

            data = response.json()

            prices = data["prices"]
            market_cap = data["market_caps"]
            volumes = data["total_volumes"]

            price_df = pd.DataFrame(prices, columns=["timestamp", "price"])
            market_df = pd.DataFrame(market_cap, columns=["timestamp", "market_cap"])
            volume_df = pd.DataFrame(volumes, columns=["timestamp", "total_volume"])

            temp_df = price_df.merge(market_df , on="timestamp")
            temp_df = temp_df.merge(volume_df , on="timestamp")

            temp_df["date"] = pd.to_datetime(temp_df["timestamp"], unit="ms")
            temp_df["coin"] = coin

            coins_data.append(temp_df)

        elif response.status_code == 429:
            print("Rate limit reached. Waiting...")
            time.sleep(30)

        else:
            print(f"Error fetching {coin}: {response.status_code}")

        time.sleep(2)

    main_df = pd.concat(coins_data , ignore_index=True)  # concatenate all dataframe in one ignoring index

    main_df.to_csv(
        path_or_buf="/data/raw_data.csv",
        index=False,
        mode="w"

    )

except JSONDecodeError:
    print("Invalid json output from api")
