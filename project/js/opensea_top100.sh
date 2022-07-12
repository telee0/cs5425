#!/bin/bash

# [20220402]
#
# script scheduled to collect data from public sources
#

cd /home/cs4225/js

yyyymmddhhmm=`date +%Y%m%d%H%M`

dataFile="/home/cs4225/data/opensea_top100-$yyyymmddhhmm.json"
logFile="/home/cs4225/logs/opensea_top100-$yyyymmddhhmm.log"

echo === `date` >> $logFile

# /usr/bin/node opensea_top100.js >> $dataFile
/usr/bin/node opensea_top100_slug.js >> $dataFile


#
# update the slug list (json) for collection stats
#

cd /home/cs4225/data

ln -f -s $dataFile opensea_top100.json
ln -f -s $dataFile opensea_top100_slug.json


exit
