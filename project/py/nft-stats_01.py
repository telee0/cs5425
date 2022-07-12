"""

CS4225/5425 project

[2022032901]

NFT Stats
https://www.nft-stats.com/top-collections/24h

"""

import requests
import pandas as pd

url = "https://www.nft-stats.com/top-collections/24h"

headers = {"Accept": "application/json"}

response = requests.request("GET", url, headers=headers)

tables = pd.read_html(response.text)

for table in tables:
    print("--------- " * 8)
    print(table)