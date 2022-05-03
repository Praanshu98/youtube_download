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

mysql_cursor.execute("SELECT urls FROM playlist_urls")
urls = mysql_cursor.fetchall()

logging.info(f"URLs found in DB: {urls}")

for url in urls:

    playlist = Playlist(url[0])

    logging.info("-"*100)

    logging.info(f'Working on playlist: {playlist.title}')

    for url in playlist.video_urls:

        logging.info(f"Working on video of : {url}")

        yt = YouTube(url)

        video_id=extract.video_id(url)

        # Fetching all the video_ids previously downloaded from youtube_url table

        mysql_cursor.execute("SELECT video_id FROM youtube_urls")

        video_ids = mysql_cursor.fetchall()

        logging.info(f"Working on ID: {video_id}")
        
        # logging.info(f"Video ids stored in DB: {video_ids}")

        # print("ID: ", video_id)

        # print("Video ID: ", video_ids)

        # Checking if the video_id is present in our table.

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

            downloader()

            audio_video_merger(playlist.title)

            # Creating an entry of the video downloaded

            qry = "INSERT INTO youtube_urls (playlist_name, video_id, video_name, video_url) VALUES (%s, %s, %s, %s)"
            val = (f"{playlist.title}", f"{video_id}", f"{video_title}", f"{url}")

            mysql_cursor.execute(qry, val)

            connect_database.db.commit()
            

        


