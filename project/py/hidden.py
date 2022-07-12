"""

CS4225/5425 project

[2022032901]


MySQL setup

https://dev.mysql.com/doc/connector-python/en/connector-python-introduction.html
https://dev.mysql.com/doc/connector-python/en/connector-python-installation-binary.html


$ pip install mysql-connector-python

mysql> create database cs4225;
mysql> CREATE USER 'cs4225'@'localhost' IDENTIFIED BY 'password';
mysql> CREATE USER 'cs4225'@'192.168.1.155' IDENTIFIED BY 'password';
mysql> GRANT ALL ON *.* TO 'cs4225'@'localhost';
mysql> GRANT ALL ON *.* TO 'cs4225'@'192.168.1.155';
mysql> FLUSH PRIVILEGES;

"""


mysql = {
    'user': 'cs4225',
    'password': 'password',
    'host': '127.0.0.1',
    # 'host': '192.168.1.24',
    'database': 'cs4225'
}

"""

** Twitter APIv2 only

https://docs.tweepy.org/en/stable/client.html

"""

twitter = {
    'consumer_key': "",
    'consumer_secret': "",
    'access_token': "",
    'access_token_secret': "",
    'bearer_token': ""
                    ""
}

opensea = {
    'api_key': ""
}

#
# End
