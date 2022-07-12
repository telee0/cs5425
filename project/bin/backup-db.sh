#!/bin/bash

#
# [2022041301]
#
# script to backup DB
#

yyyymmdd=`date +%Y%m%d`

cd /home/cs4225

user="root"
dbname="cs4225"

/usr/bin/mysqldump \
        --force --quick \
        --skip-opt --create-options \
        --add-drop-table \
        --extended-insert \
	--user=$user \
        $dbname > backup/$dbname-$yyyymmdd.sql

/usr/bin/bzip2 -9 backup/*.sql &


exit
        --host=$host --port=$port \
        --user=$user --password=$password \
        --default-character-set=utf-8 \
