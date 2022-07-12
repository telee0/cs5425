#!/bin/bash

#
# [2022041201]
#
# Script to retrieve OpenSea events
#
# https://docs.opensea.io/reference/retrieving-asset-events
#

API_KEY=''

CURL=/usr/bin/curl
P3=/usr/bin/python3


d=`date +%Y%m%d_%H%M%S`

yyyymmdd="`echo $d | cut -c1-8`"
yyyymm="`echo $yyyymmdd | cut -c1-6`"
yyyy="`echo $yyyymmdd | cut -c1-4`"
dd="`echo $yyyymmdd | cut -c7-8`"

DATA_DIR="/home/cs4225/data/$yyyymm/$dd"
DATA_FILE="$DATA_DIR/opensea_event-$d.json"
LOG_DIR="/home/cs4225/logs/$yyyymm/$dd"
LOG_FILE="$LOG_DIR/opensea_event-$d.log"

[ ! -d $DATA_DIR ] && mkdir -p $DATA_DIR
[ ! -d $LOG_DIR  ] && mkdir -p $LOG_DIR


EVENT_TYPE="successful"
s=`date -d "-5 minutes" +%s`
URL="https://api.opensea.io/api/v1/events?event_type=$EVENT_TYPE&occurred_after=$s"

$CURL --request GET --url $URL \
	--header 'Accept: application/json' \
	--header "X-API-KEY: $API_KEY" \
	--silent \
	--output $DATA_FILE


#
# python script to load data from the json file to db and generate csv
#

$P3 /home/cs4225/py/opensea_event.py $DATA_FILE > $LOG_FILE


exit

