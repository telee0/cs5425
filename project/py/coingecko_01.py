"""

CS4225/5425 project

[2022032901]

Web spider bot to extract data from https://www.coingecko.com/en/nft.

"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
import hashlib
from datetime import datetime


def get_nft(count):
    resp = requests.get(f'https://www.coingecko.com/en/nft?page={count}')
    soup = BeautifulSoup(resp.text, 'html.parser')
    table = soup.find('table', {'class': 'sort table mb-0 text-sm text-lg-normal table-scrollable'})

    if table:
        rows = table.find_all('tr')
        colname = [x.get_text(strip=True) for x in rows[0].find_all('th')]
        href = [["https://www.coingecko.com"+y['href'] for y in x.find_all('a')] for x in rows[1:]]
        img = [[y['src'] for y in x.find_all('img')] for x in rows[1:]]
        data = [{col: row.get_text(strip=True) for col, row in zip(colname, x.find_all('td'))} for x in rows[1:]]

        for x, y, z in zip(data, img, href):
            x['img'] = y[0]
            x['href'] = z[0]
        return pd.DataFrame(data)
    else:
        return pd.DataFrame()


def hashing(key):

    return hashlib.md5(key.encode('utf-8')).hexdigest()


df = []
for i in range(1, 10):
    data = get_nft(i)
    if not data.empty:
        df.append(data)
    else:
        break

df = pd.concat(df)
df['hash'] = df['NFT'].apply(lambda x: hashing(x))
print(df.info())

df.to_csv("data/coingecko-{}.csv".format(datetime.now().strftime('%Y%m%d%H%M')))
