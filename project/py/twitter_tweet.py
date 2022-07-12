"""

CS4225/5425 project

[2022032901]

** Twitter APIv2 only

https://docs.tweepy.org/en/stable/client.html#tweepy.Client.search_recent_tweets
https://docs.tweepy.org/en/stable/client.html

"""

import csv
import json
import mysql_ as my
import time
import tweepy
from datetime import datetime
from hidden import twitter as tw
from mysql_ import db_fields as dbf
from os import makedirs

verbose, debug = True, False


# function for generating json path
#


def json_file():
    t = datetime.now().strftime('%Y%m%d_%H%M')
    yyyymm = t[0:6]
    dd = t[6:8]
    # path = "data/tweets/{0}/{1}".format(yyyymm, dd)
    path = "/home/cs4225/data/tweets/{0}/{1}".format(yyyymm, dd)
    makedirs(path, exist_ok=True)
    return "{0}/tw_tweet-{1}.json".format(path, t)


# tweepy call for tweets (Twitter API v2) with a set of search criteria
#
client = tweepy.Client(tw["bearer_token"], return_type=dict)

# Twitter query parameters
#
# https://docs.tweepy.org/en/stable/client.html?#search-tweets
# https://developer.twitter.com/en/docs/twitter-api/tweets/search/integrate/build-a-query#examples
#

# query = "#nft"
end_time = None
expansions = ["author_id"]
max_results = 10
media_fields = None
next_token = None
place_fields = None
poll_fields = None
since_id = None
sort_order = None
start_time = None
tweet_fields = ['id', 'text', 'author_id', 'conversation_id', 'created_at', 'entities', 'in_reply_to_user_id',
                'public_metrics']
until_id = None
user_fields = [
    "created_at", "description", "entities",
    "id", "location", "name", "pinned_tweet_id", "profile_image_url",
    "public_metrics", "url", "username"]

slug_list = my.db_cmd('getOpenSeaTop100Slug')
query_list = [x[0] for x in slug_list]
query_list.append('#nft')

# include users from opernsea_top100
#
name_list = my.db_cmd('getOpenSeaTwitterUsername')
query_list.extend(["from:{}".format(x[0]) for x in name_list])

if verbose:
    print(query_list)

if verbose:
    print("query_list: {0} ({1})".format(query_list, len(query_list)))

for query in query_list:
    if verbose:
        print("=== query:", query)

    try:
        response = client.search_recent_tweets(query,
                                               end_time=end_time, expansions=expansions, max_results=max_results,
                                               media_fields=media_fields, next_token=next_token,
                                               place_fields=place_fields, poll_fields=poll_fields, since_id=since_id,
                                               sort_order=sort_order, start_time=start_time, tweet_fields=tweet_fields)
    except tweepy.TweepyException as e:
        print("query: {0}: {1}".format(query, e))
        continue

    if verbose and 'data' not in response:
        print("response:", response)
        continue

    json_file_name = json_file()
    csv_file_name = json_file_name.replace('.json', '.csv')

    tweet_dict, rows = {}, []

    if debug:
        print(response['data'])

    for i, tweet in enumerate(response['data']):
        print('--------- ' * 8, "[{0}] {1}".format(i, query))

        tweet_dict = {}

        for field in tweet:
            if field in ['entities', 'public_metrics']:
                for key in tweet[field]:
                    # dict_key = field + '_' + key
                    dict_key = key
                    tweet_dict[dict_key] = tweet[field][key]
                    print("{0}: {1}".format(dict_key, tweet[field][key]))
            else:
                tweet_dict[field] = tweet[field]
                print("{0}: {1}".format(field, tweet_dict[field]))

        tweet_dict['tweet_id'] = tweet_dict['id']
        tweet_dict['query'] = query
        tweet_dict['path'] = json_file_name

        row = []
        for field in dbf['tw_tweet']['fields']:
            if field in tweet_dict:
                row.append(tweet_dict[field])
            else:
                row.append("")
        rows.append(row)

    # generate output files
    #
    # CSV/DB for indexing the JSON files
    #
    f = open(json_file_name, 'a')
    f.write(json.dumps(response['data'], indent=4))
    f.close()

    csv_file = open(csv_file_name, 'a', encoding='UTF-8', newline='')
    w = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_ALL, quotechar='"')
    w.writerow(dbf['tw_tweet']['fields'])
    w.writerows(rows)

    # store data in database
    #
    for row in rows:
        my.db_cmd('createTwitterTweet', dbf['tw_tweet']['fields'], row)

    time.sleep(0.5)
