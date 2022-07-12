"""

CS4225/5425 project

[2022032901]

https://api-bff.nftpricefloor.com/nfts

"""

import requests
import json
import csv
from datetime import datetime
import mysql_ as my
import time
from mysql_ import db_fields as dbf

debug, verbose = False, True

def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            for i, a in enumerate(x):
                flatten(a, name + str(i) + '_')
        else:
            out[name[:-1]] = x

    flatten(y)
    return out


json_file = "data/nfts.json"

f = open(json_file, 'r')
collections = json.loads(f.read())
f.close()

if verbose: print("nftpricefloor: {0} collections".format(len(collections)))

if debug:
    print(json.dumps(collections, indent=4))

req_headers = {"Accept": "application/json"}

i, rows = 0, []

for coll in collections:
    coll_dict = flatten_json(coll)

    if verbose:
        print('--------- ' * 8)
        print("name: {0}, slug: {1}".format(coll['name'], coll['slug']))
    if debug:
        print(json.dumps(coll, indent=4))
    """
    # retrieve collection stats given slug, one at a time
    #
    url = "https://api.opensea.io/api/v1/collection/{}/stats".format(coll['slug'])

    response = requests.request("GET", url, headers=req_headers)
    data = json.loads(response.text)

    if verbose:
        if debug: print("response:", response.text)
        print("i:", i, ", data:", json.dumps(data, indent=4))
    """

    for key, value in coll_dict.items():
        print("{0}: {1} ({2})".format(key, value, type(value)))

    break

    coll_dict = data['stats']
    coll_dict.update(coll)

    row = []
    for field in dbf['opensea_top100']['fields']:
        if field in coll_dict:
            row.append(coll_dict[field])
        else:
            row.append("")
    rows.append(row)

    if verbose:
        # print(data)
        print(coll_dict)
        print(row)

    i += 1

    if i % 10 == 0:
        time.sleep(0.5)  # less aggressive to pull data

# t = datetime.now().strftime('%Y%m%d%H%M')

# generate output files
#
csv_file_name = "data/nftpricefloor-{}.csv".format(datetime.now().strftime('%Y%m%d%H%M'))
csv_file = open(csv_file_name, 'w', encoding='UTF-8', newline='')
w = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_ALL, quotechar='"')
w.writerow(dbf['opensea_top100']['fields'])
w.writerows(rows)

# store data in database
#
for row in rows:
    pass
    # my.db_cmd('createNFTPriceFloor', dbf['nftpricefloor']['fields'], row)
