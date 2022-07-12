#!/bin/bash
#
# [20220402]
#
# script scheduled to collect data from public sources
#
# supposed to run daily, but now we speed up data collection with 6-hour intervals
#

P3=/usr/bin/python3

d=`date +%Y%m%d_%H%M%S`

yyyymmdd="`echo $d | cut -c1-8`"
yyyymm="`echo $yyyymmdd | cut -c1-6`"
yyyy="`echo $yyyymmdd | cut -c1-4`"
dd="`echo $yyyymmdd | cut -c7-8`"

LOG_DIR="/home/cs4225/logs/top100/$yyyymm/$dd"
LOG_FILE="$LOG_DIR/opensea_top100-$d.log"

[ ! -d $LOG_DIR  ] && mkdir -p $LOG_DIR


cd /home/cs4225/py


$P3 opensea_top100.py >> $LOG_FILE


exit

