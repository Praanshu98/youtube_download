from pytube import YouTube

urls = ["https://www.youtube.com/watch?v=2tTthnmfl7I","https://www.youtube.com/watch?v=OzuHuZ-viRo",
"https://www.youtube.com/watch?v=XxmxHdA-VpA", "https://www.youtube.com/watch?v=tkGgnBWfVIA",
"https://www.youtube.com/watch?v=CGgcjaqRGtE", "https://www.youtube.com/watch?v=SehiWYrvZho",
"https://www.youtube.com/watch?v=C9xg5ZkQsT4"]

# urls = ["https://www.youtube.com/watch?v=2tTthnmfl7I"]


for i in range(len(urls)):

    yt = YouTube(urls[i])

    temp_video = yt.streams.filter(adaptive=True, file_extension="mp4",type="audio", abr="128kbps")
    # temp_video = yt.streams.filter(adaptive=True, file_extension="mp4",res="1080p",type="video")

    temp_video = yt.streams.get_by_itag(137).download(filename_prefix="Video_", filename=f"{i}.mp4")
    temp_video = yt.streams.get_by_itag(140).download(filename_prefix="Audio_", filename=f"{i}.mp4")

    print(temp_video)

    print("-"*20)