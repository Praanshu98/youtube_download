from pytube import YouTube
from pytube import Playlist
from pytube import extract
import os
import connect_database
import logging
import re

logging.basicConfig(filename='example.log', level=logging.DEBUG)

mysql_cursor = connect_database.db.cursor()

playlist = Playlist('https://www.youtube.com/playlist?list=PL9-I-e3B9DhG6x_sVLXbCzUPxI3MDQI7L')

logging.info("-"*100)

for url in playlist.video_urls:

    logging.info(f'Downloading: {playlist.title}')

    logging.info(" Downloading video of : {url}")

    yt = YouTube(url)

    video_id=extract.video_id(url)

    mysql_cursor.execute("SELECT video_id FROM youtube_urls")

    video_ids = mysql_cursor.fetchall()

    logging.info(f"Working on ID: {video_id}")
    
    # logging.info(f"Video ids stored in DB: {video_ids}")

    # print("ID: ", video_id)

    # print("Video ID: ", video_ids)

    
    for id in video_ids:
        if video_id == id[0]:
            logging.info(f"{video_id} found, checking next id")
            break
    else:
        video_title = yt.title

        # change below code, check and replace for all special characters

        video_title = re.sub('[^a-zA-Z0-9\n\.]', '', video_title)

        print(video_title)

        # temp_video = yt.streams.filter(adaptive=True, file_extension="mp4",type="audio", abr="128kbps")
        # temp_video = yt.streams.filter(adaptive=True, file_extension="mp4",res="1080p",type="video")

        qry = "INSERT INTO youtube_urls (playlist_name, video_id, video_name, video_url) VALUES (%s, %s, %s, %s)"
        val = (f"{playlist.title}", f"{video_id}", f"{video_title}", f"{url}")

        mysql_cursor.execute(qry, val)

        connect_database.db.commit()

        video = yt.streams.get_by_itag(137).download(filename_prefix="Video_", filename=f"{video_title}.mp4")

        logging.info(f"{video}")

        logging.info("-"*50)

        audio = yt.streams.get_by_itag(140).download(filename_prefix="Audio_", filename=f"{video_title}.mp4")

        logging.info("-"*50)

        os.system(f"ffmpeg -i Video_{video_title}.mp4 -i Audio_{video_title}.mp4 -c copy {video_title}.mp4")

	