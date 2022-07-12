"""

CS4225/5425 project

[2022032901]

https://dev.mysql.com/doc/connector-python/en/connector-python-introduction.html
https://dev.mysql.com/doc/connector-python/en/connector-python-installation-binary.html


db command types

D - Delete
F - Find
I - Insert
S - Select
U - Update

"""


db_queries = {
    'createOpenSeaTop100Old': {
        'type': 'I',
        'sql': (
            'INSERT INTO opensea_top100_old (%s, created) VALUES (%s, NOW())'
        )

    },
    'createOpenSeaTop100': {
        'type': 'I',
        'sql': (
            'INSERT INTO opensea_top100 (%s, created) VALUES (%s, NOW())'
        )

    },
    'createOpenSeaEvent': {
        'type': 'I',
        'sql': (
            'INSERT INTO opensea_event (%s, created) VALUES (%s, NOW())'
        )

    },
    'createTwitterUser': {
        'type': 'I',
        'sql': (
            'INSERT INTO tw_user (%s, created) VALUES (%s, NOW())'
        )
    },
    'createTwitterTweet': {
        'type': 'I',
        'sql': (
            'INSERT INTO tw_tweet (%s, created) VALUES (%s, NOW())'
        )
    },
    'getOpenSeaTop100Slug': {
        'type': 'S',
        'sql': (
            'SELECT slug FROM opensea_top100 ORDER BY id DESC LIMIT 10'
        )
    },
    'getOpenSeaTwitterUsername': {
        'type': 'S',
        'sql': (
            'SELECT twitter_username, MAX(id) AS max_id '
            'FROM opensea_top100 WHERE twitter_username IS NOT NULL '
            'GROUP BY twitter_username ORDER BY max_id DESC LIMIT 100'
        )
    }
}
