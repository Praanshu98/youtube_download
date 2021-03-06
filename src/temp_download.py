from pytube import YouTube
import os


# urls = ["https://www.youtube.com/watch?v=2tTthnmfl7I","https://www.youtube.com/watch?v=OzuHuZ-viRo",
# "https://www.youtube.com/watch?v=XxmxHdA-VpA", "https://www.youtube.com/watch?v=tkGgnBWfVIA",
# "https://www.youtube.com/watch?v=CGgcjaqRGtE", "https://www.youtube.com/watch?v=SehiWYrvZho",
# "https://www.youtube.com/watch?v=C9xg5ZkQsT4"]

#urls = ["https://www.youtube.com/watch?v=MQWNuNRPU6c", "https://www.youtube.com/watch?v=uqAmbKOz_x0"
#,"https://www.youtube.com/watch?v=8AwIJZj07s8", "https://www.youtube.com/watch?v=Zv11L-ZfrSg",
#"https://www.youtube.com/watch?v=LXb3EKWsInQ"]

urls = ["https://www.youtube.com/watch?v=LXb3EKWsInQ"]


for i in range(len(urls)):

	yt = YouTube(urls[i])

	# temp_video = yt.streams.filter(adaptive=True, file_extension="mp4",type="audio", abr="128kbps")
	# temp_video = yt.streams.filter(adaptive=True, file_extension="mp4",res="1080p",type="video")

	#temp_video = yt.streams.filter(adaptive=True,file_extension="mp4")

	temp_video = yt.streams.get_by_itag(401).download(filename_prefix="Video_", filename=f"{i}.mp4")

	print(temp_video)

	print("-"*50)

	temp_video = yt.streams.get_by_itag(140).download(filename_prefix="Audio_", filename=f"{i}.mp4")

	print(temp_video)

	print("-"*50)

	os.system(f"ffmpeg -i Video_{i}.mp4 -i Audio_{i}.mp4 -c copy output_{i}.mp4")

	os.system(f"scp output_{i}.mp4 192.168.1.107:/Users/praanshu/Desktop/test")

	print("-"*50)
