#!/bin/bash

FILE=/home/praanshu/yt_downloader/script_running.txt
if [ -f "$FILE" ]; then
    echo "$FILE exists."
    echo "Script is running"
else 
    echo "$FILE does not exist, creating one now"
    touch /home/praanshu/yt_downloader/script_running.txt
    echo " Starting Script "
    source /home/praanshu/anaconda3/bin/activate youtube &&
    cd /home/praanshu/yt_downloader/ && python src/playlist_download.py
    rm -rf /home/praanshu/yt_downloader/script_running.txt
    echo "$FILE deleted"
fi

