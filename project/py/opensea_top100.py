"""

CS4225/5425 project

[2022032901]

OpenSea API v1

https://docs.opensea.io/reference/retrieving-collection-stats

"""


import csv
import json
import mysql_ as my
import requests
import time
from datetime import datetime
from hidden import opensea as op
from mysql_ import db_fields as dbf
from os import makedirs


debug, verbose = False, True


def json_file():
    t = datetime.now().strftime('%Y%m%d_%H%M')
    yyyymm = t[0:6]
    dd = t[6:8]
    # path = "data/top100/{0}/{1}".format(yyyymm, dd)
    path = "/home/cs4225/data/top100/{0}/{1}".format(yyyymm, dd)
    makedirs(path, exist_ok=True)
    return "{0}/opensea_top100-{1}.json".format(path, t)


# read the input json file for the slug list (collected through a js script)
#
slug_file_name = "/home/cs4225/data/opensea_top100_slug.json"

f = open(slug_file_name, 'r', encoding="utf-8")
collections = json.loads(f.read())
f.close()

if debug:
    print(json.dumps(collections, indent=4))

# extract the slug list from the top 100 list
#
slug_list = []

for coll in collections:
    slug_list.append(coll['slug'])

if verbose:
    print("opensea_top100: {0} collections".format(len(slug_list)))


req_headers = {"Accept": "application/json", "X-API-KEY": op['api_key']}

i, rows, coll_data = 0, [], []

for slug in slug_list:

    if debug and i == 5:
        break

    if verbose:
        print('--------- ' * 8, "[{0}] {1}".format(i, slug))
        # print(json.dumps(coll, indent=4))

    # retrieve collection stats given slug, one at a time
    #
    url = "https://api.opensea.io/api/v1/collection/{}".format(slug)

    response = requests.request("GET", url, headers=req_headers)
    data = json.loads(response.text)
    coll = data['collection']
    coll_data.append(coll)

    if debug:
        for key in coll.keys():
            print("{0}: {1}".format(key, coll[key]))

    coll_dict = {}

    for field in coll['stats']:
        coll_dict[field] = coll['stats'][field]

    coll_dict['logo'] = coll['image_url']

    for field in dbf['opensea_top100']['fields']:
        if field not in coll_dict and field in coll:
            coll_dict[field] = coll[field]

    for field in coll_dict:
        print("{0}: {1}".format(field, coll_dict[field]))

    row = []
    for field in dbf['opensea_top100']['fields']:
        if field in coll_dict:
            row.append(coll_dict[field])
        else:
            row.append("")
    rows.append(row)

    i += 1

    if i % 10 == 0:
        time.sleep(0.5)  # less aggressive to pull data

# t = datetime.now().strftime('%Y%m%d%H%M')

# prepare the output json file
#
json_file_name = json_file()
f = open(json_file_name, 'a')
f.write(json.dumps(coll_data, indent=4))
f.close()

# generate output files
#
csv_file_name = json_file_name.replace('.json', '.csv')
csv_file = open(csv_file_name, 'w', encoding='UTF-8', newline='')
w = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_ALL, quotechar='"')
w.writerow(dbf['opensea_top100']['fields'])
w.writerows(rows)

# store data in database
#
for row in rows:
    my.db_cmd('createOpenSeaTop100', dbf['opensea_top100']['fields'], row)
