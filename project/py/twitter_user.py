"""

CS4225/5425 project

[2022032901]

** Twitter APIv2 only

https://docs.tweepy.org/en/stable/client.html

"""


import csv
import mysql_ as my
import re
import tweepy
from datetime import datetime
from hidden import twitter as tw
from mysql_ import db_fields as dbf
from targets import targets


verbose = True


client = tweepy.Client(tw["bearer_token"])

# https://developer.twitter.com/en/docs/twitter-api/users/lookup/api-reference/get-users
#
# user_ids = [946213559213555712]
#
user_fields = [
    "created_at", "description", "entities",
    "id", "location", "name", "pinned_tweet_id", "profile_image_url",
    "public_metrics", "url", "username"
]

# initialize with a static target list
#
user_set = set(targets)

# include users from opernsea_top100
#
name_list = my.db_cmd('getOpenSeaTwitterUsername')
user_set.update({x[0] for x in name_list})

user_list = list(user_set)

# check username format
#
p = re.compile('^[A-Za-z0-9_]{1,15}$')

usernames = []

for username in user_list:
    if p.match(username):
        usernames.append(username)
    elif verbose:
        print("{0}: username does not match ^[A-Za-z0-9_]{{1,15}}$".format(username))

if verbose:
    print("targets =", usernames)

response = client.get_users(
    # ids=user_ids,
    usernames=usernames, user_fields=user_fields
)

user_dict, rows = {}, []

for i, user in enumerate(response.data):
    print('--------- ' * 8, "[{0}] {1}".format(i, user))

    user_dict = {}

    for field in user:
        if field in {'entities', 'public_metrics'}:
            continue
        value = getattr(user, field)
        user_dict[field] = value
        print("user.{0}: {1}".format(field, value))
    if user.entities is not None:
        for key in user.entities:
            user_dict['e_' + key] = user.entities[key]
            print("entities: key: {0}, value: {1} ({2})".format(key, user.entities[key], len(user.entities[key])))
    for key in user.public_metrics:
        user_dict[key] = user.public_metrics[key]
        print("public_metrics: key: {0}, value: {1}".format(key, user.public_metrics[key]))

    user_dict['user_id'] = user_dict['id']

    if verbose:
        print()
        for key in user_dict.keys():
            print("user_dict.key: {0}, value: {1}, type: {2}".format(key, user_dict[key], type(user_dict[key])))
        print(type(user_dict['description']))

    row = []
    for field in dbf['tw_user']['fields']:
        if field in user_dict:
            row.append(user_dict[field])
        else:
            row.append("")
    rows.append(row)

# t = datetime.now().strftime('%Y%m%d%H%M')

# generate output files
#
csv_file_name = "data/tw_user/tw_user-{}.csv".format(datetime.now().strftime('%Y%m%d%H%M'))
csv_file = open(csv_file_name, 'w', encoding='UTF-8', newline='')
w = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_ALL, quotechar='"')
w.writerow(dbf['tw_user']['fields'])
w.writerows(rows)

# store data in database
#
for row in rows:
    my.db_cmd('createTwitterUser', dbf['tw_user']['fields'], row)
