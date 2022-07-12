#!/bin/bash
#
# [20220402]
#
# script scheduled to collect data from public sources
#
# the py script searches tweets with slug from db table opensea_top100
#

P3=/usr/bin/python3

d=`date +%Y%m%d_%H%M%S`

yyyymmdd="`echo $d | cut -c1-8`"
yyyymm="`echo $yyyymmdd | cut -c1-6`"
yyyy="`echo $yyyymmdd | cut -c1-4`"
dd="`echo $yyyymmdd | cut -c7-8`"

LOG_DIR="/home/cs4225/logs/tweets/$yyyymm/$dd"
LOG_FILE="$LOG_DIR/tw_tweet-$d.log"

[ ! -d $LOG_DIR  ] && mkdir -p $LOG_DIR


cd /home/cs4225/py


$P3 twitter_tweet.py >> $LOG_FILE


exit

