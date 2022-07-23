#!/bin/bash

FILE=/home/praanshu/yt_downloader/script_running.txt
if [ -f "$FILE" ]; then
    echo "$FILE exists."
    echo "Script is running"
else 
    echo "$FILE does not exist."
    echo " Starting Script "
    source /home/praanshu/anaconda3/bin/activate youtube &&
    cd /home/praanshu/yt_downloader/ && python src/playlist_download.py
    rm /home/praanshu/yt_downloader/script_running.txt
    echo "$File deleted"
fi

