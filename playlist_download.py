from pytube import YouTube
from pytube import Playlist
import os

p = Playlist('https://www.youtube.com/playlist?list=PL9-I-e3B9DhG6x_sVLXbCzUPxI3MDQI7L')

print(f'Downloading: {p.title}')

for url in p.video_urls:
    print(" Downloading video of :",url)

    yt = YouTube(url)

    video_name = yt.title

    video_name = video_name.replace(" ", "_")
    video_name = video_name.replace("(", "_")
    video_name = video_name.replace(")", "_")
    video_name = video_name.replace("-", "_")

    print(video_name)

    # temp_video = yt.streams.filter(adaptive=True, file_extension="mp4",type="audio", abr="128kbps")
    # temp_video = yt.streams.filter(adaptive=True, file_extension="mp4",res="1080p",type="video")

    temp_video = yt.streams.get_by_itag(137).download(filename_prefix="Video_", filename=f"{video_name}.mp4")

    print(temp_video)

    print("-"*50)

    temp_video = yt.streams.get_by_itag(140).download(filename_prefix="Audio_", filename=f"{video_name}.mp4")

    print(temp_video)

    print("-"*50)

    os.system(f"ffmpeg -i Video_{video_name}.mp4 -i Audio_{video_name}.mp4 -c copy {video_name}.mp4")

    print("-"*50)



