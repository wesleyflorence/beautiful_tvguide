#!/bin/sh

echo $(date) >> bash_cron_log.txt
/usr/bin/python3 /home/wes/WibbleWobble/beautiful_tvguide/tvguide.py >> bash_cron_log.txt

