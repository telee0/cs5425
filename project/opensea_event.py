"""

CS4225/5425 project

[2022032901]

OpenSea API v1

https://docs.opensea.io/reference/retrieving-asset-events
https://docs.opensea.io/reference/retrieving-collection-stats

"""

import csv
import json
import mysql_ as my
import sys
from mysql_ import db_fields as dbf

verbose, debug = True, False


# https://towardsdatascience.com/flattening-json-objects-in-python-f5343c794b10
#

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


# capture the command line arguments
#

argc = len(sys.argv)
if argc > 1:
    json_file_name = sys.argv[1]
    if argc > 2:
        print("{0}: only the first data file is read..".format(sys.argv[0]))
else:
    sys.exit("{0}: data file not specified".format(sys.argv[0]))

# json_file_name = "data/opensea_event-20220412_122501.json"

try:
    f = open(json_file_name, 'r', encoding="utf-8")
    j = json.loads(f.read())
except IOError as e:
    sys.exit("{0}: {1}".format(json_file_name, e))
except:
    sys.exit("{0}: unknown error".format(json_file_name))
finally:
    f.close()


events = j["asset_events"]

rows = []

for idx, event in enumerate(events):
    event_dict = flatten_json(event)
    if verbose:
        if 'asset_name' in event_dict:
            asset_name = event_dict['asset_name']
        else:
            asset_name = "event_id ({})".format(event_dict['id'])
        print("--------- " * 8, "[{0}] {1}".format(idx, asset_name))
        # print(event_dict)
        for key, value in event_dict.items():
            print("{0}: {1}".format(key, value))
    if debug:
        print("', '".join(event_dict.keys()))

    event_dict['event_id'] = event_dict['id']

    row = []
    for field in dbf['opensea_event']['fields']:
        if field in event_dict:
            row.append(event_dict[field])
        else:
            row.append("")
    rows.append(row)

# generate output files
#
# csv_file_name = "data/opensea_event-{}.csv".format(datetime.now().strftime('%Y%m%d_%H%M'))
csv_file_name = json_file_name.replace('.json', '.csv')
csv_file = open(csv_file_name, 'w', encoding='UTF-8', newline='')
w = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_ALL, quotechar='"')
w.writerow(dbf['opensea_event']['fields'])
w.writerows(rows)

# store data in database
#
for row in rows:
    my.db_cmd('createOpenSeaEvent', dbf['opensea_event']['fields'], row)
