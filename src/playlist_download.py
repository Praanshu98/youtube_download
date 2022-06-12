from pytube import YouTube
from pytube import Playlist
from pytube import extract
import os
import connect_database
import directory_checker
import logging
import re

directory_checker.folder_checker()


logging.basicConfig(filename='logs/example.log', level=logging.DEBUG)

mysql_cursor = connect_database.db.cursor()

def downloader():

    video = yt.streams.get_by_itag(137).download(filename_prefix="temp/Video_", filename=f"{video_title}.mp4")

    logging.info(f"{video}")

    logging.info("-"*100)

    audio = yt.streams.get_by_itag(140).download(filename_prefix="temp/Audio_", filename=f"{video_title}.mp4")

    logging.info("-"*100)

def audio_video_merger(title):

    ifdir = os.path.isdir(f"{os.getcwd()}/videos/{title}")

    if ifdir == False:
        os.system(f"mkdir videos/{title}")
        print(f"{title} folder created")
    
    os.system(f"ffmpeg -i temp/Video_{video_title}.mp4 -i temp/Audio_{video_title}.mp4 -c copy videos/{title}/{video_title}.mp4")

    os.system(f"rm -rf temp/Audio_* temp/Video_*")

# Fetching all the urls from playlist_urls table

mysql_cursor.execute("SELECT playlist_URL FROM playlist_urls")
playlist_urls = mysql_cursor.fetchall()

logging.info(f"URLs found in DB: {playlist_urls}")

for url in playlist_urls:

    playlist = Playlist(url[0])

    logging.info("-"*100)

    logging.info(f'Working on playlist: {playlist.title}')

    for video_url in playlist.video_urls:

        logging.info(f"Working on video of : {video_url}")

        yt = YouTube(video_url)

        video_id=extract.video_id(video_url)

        # Fetching all the video_ids previously downloaded from youtube_url table

        mysql_cursor.execute("SELECT yt_video_id FROM video_urls")

        video_ids = mysql_cursor.fetchall()

        logging.info(f"Working on ID: {video_id}")

        # Checking if the video_id is present in our table.

        for id in video_ids:
            if video_id == id[0]:
                logging.info(f"{video_id} found, checking next id")
                break
        else:
            video_title = yt.title

            # change below code, check and replace for all special characters

            video_title = re.sub('[^a-zA-Z0-9\n\.]', '', video_title)

            logging.info(f"Video id: " + video_id)


            downloader()

            audio_video_merger(playlist.title)

            # Creating an entry of the video downloaded
            
            qry = f'select id from playlist_urls where playlist_name = "{str(playlist.title)}"'

            mysql_cursor.execute(qry)

            playlist_id = mysql_cursor.fetchall()

            playlist_id = playlist_id[0][0]

            qry = "INSERT INTO video_urls (playlist_id, yt_video_id, video_name, video_url) VALUES (%s, %s, %s, %s)"
            val = (f"{playlist_id}", f"{video_id}", f"{video_title}", f"{video_url}")
            mysql_cursor.execute(qry, val)

            connect_database.db.commit()

