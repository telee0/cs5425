#!/bin/bash

d=`date +%Y%m%d_%H%M%S`

yyyymmdd="`echo $d | cut -c1-8`"
yyyymm="`echo $yyyymmdd | cut -c1-6`"
yyyy="`echo $yyyymmdd | cut -c1-4`"
dd="`echo $yyyymmdd | cut -c7-8`"

LOG_DIR="/home/cs4225/logs/top100_image/$yyyymm/$dd"
LOG_FILE="$LOG_DIR/opensea_top100_image-$yyyymmdd.log"
DATA_DIR="/home/cs4225/data/top100_image/$yyyymm/$dd"
DATA_FILE="$DATA_DIR/opensea_top100_image-$yyyymmdd.txt"

[ ! -d $LOG_DIR  ] && mkdir -p $LOG_DIR
[ ! -d $DATA_DIR  ] && mkdir -p $DATA_DIR

M="/usr/bin/mysql"
W="/usr/bin/wget"

cd /home/cs4225/sql

$M -u root cs4225 \
	--skip-column-names < top100_image.sql >> $DATA_FILE

IFS=$'\n'

for line in `cat top100_image.txt`; do
	id=`echo $line | cut -f1`
	url=`echo $line | cut -f2`
	echo id == $id
	echo url == $url
	$W "$url" -O "$DATA_DIR/$id" -a $LOG_FILE
done

