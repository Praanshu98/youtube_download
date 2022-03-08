from pytube import YouTube

# #where to save
# SAVE_PATH = "./" #to_do

# #link of the video to be downloaded
# link=["https://www.youtube.com/watch?v=xWOoBJUqlbI",
# 	"https://www.youtube.com/watch?v=xWOoBJUqlbI"
# 	]

# for i in link:
# 	try:
		
# 		# object creation using YouTube
# 		# which was imported in the beginning
# 		yt = YouTube(i)
# 	except:
		
# 		#to handle exception
# 		print("Connection Error")
	
# 	#filters out all the files with "mp4" extension
# 	mp4files = yt.filter('mp4')
# 	mp4files = yt.filter

# 	# get the video with the extension and
# 	# resolution passed in the get() function
# 	d_video = yt.get(mp4files[-1].extension,mp4files[-1].resolution)
# 	try:
# 		# downloading the video
# 		d_video.download(SAVE_PATH)
# 	except:
# 		print("Some Error!")
# print('Task Completed!')

URL = ["https://www.youtube.com/watch?v=2tTthnmfl7I"]

for i in URL:

	video = YouTube(i)
	video_streams = video.streams.filter(file_extension='mp4').get_by_itag(137)
	video_streams.download(filename = "1.mp4",
		output_path = "video_path")