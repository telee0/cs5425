#
# CS4225/5425 project - Data Lake
#
# [20220313]
#

README.txt		- this file
backup			- folder for data and logs backup
bin			- folder for utility scripts
data			- folder for data collection
data-events		- link to event data under data/
data-top100		- link to collection data under data/top100/
data-top10_image	- link to collection data under data/top100_image/
data-tweets		- link to searched tweets under data/tweets/
docs			- folder for documentation
js			- folder for JS scripts
logs			- folder for job logs
mysql			- folder for DBMS (MySQL)
py			- folder for Python scripts
sql			- folder for SQL files
tmp			- tmp folder


################################################################################

/etc/crontab
#
# script to collect OpenSea top 100 collections
#
35  */6 * * *   root    /home/cs4225/py/opensea_top100.sh
#
# script to collect OpenSea events every 5 minutes
#
*/5 *   * * *   root    /home/cs4225/py/opensea_event.sh

root@marcus-4225-proj-1:~/cs4225/js# ls -la /etc/cron.hourly/
total 12
drwxr-xr-x   2 root root 4096 Apr 16 06:50 .
drwxr-xr-x 106 root root 4096 Apr 13 22:44 ..
-rw-r--r--   1 root root  102 Aug  6  2021 .placeholder
lrwxrwxrwx   1 root root   33 Apr  3 21:33 opensea_top100 -> /home/cs4225/js/opensea_top100.sh
lrwxrwxrwx   1 root root   32 Apr 15 01:02 twitter_tweet -> /home/cs4225/py/twitter_tweet.sh
lrwxrwxrwx   1 root root   31 Apr 16 06:50 twitter_user -> /home/cs4225/py/twitter_user.sh

################################################################################

# scripts for data collection and processing
#

content in ./py

README.txt		- this file
backup-20220402		- backup of old scripts
coingecko_01.py		- data collection with CoinGecko, currently not scheduled
data			- link to data folder for data collection
data-events		- link to event data under data/
hidden.py		- secret file for API access
logs			- link to folder for job logs
mysql_.py		- Python script for DB access (MySQL)
mysql_q.py		- Python script for DB access (MySQL queries)
nft-stats_01.py		- data collection with NFT Stats https://www.nft-stats.com/, currently not scheduled
opensea_event.py	- Python script for data collection (event aka sales) with OpenSea
opensea_event.sh	- BASH script to automate the process
opensea_top100.py	- Python script for data collection (top 100 collections) with OpenSea
opensea_top100.sh	- BASH script to automate the process
targets.py		- Python script to contain twitter user names as tracing targets (static for initialization)
twitter_tweet.py	- Python script for data collection (recent tweets with query) with Twitter
twitter_tweet.sh	- BASH script to automate the process
twitter_user.py		- Python script for data collection (Twitter users) with Twitter, from both targets and top100
twitter_user.sh		- BASH script to automate the process


content in ./js

opensea_top100.js	- JS script to 
opensea_top100.sh	- BASH script to automate the process
opensea_top100_slug.js
opensea_twitter_users.js
