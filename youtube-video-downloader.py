#kapeed
#import required module pytube > use "pip install pytube" to install the module first
import pytube

video_url= input("Enter the url of the video:  ") #provide the url of the video
download_location = input("Enter the download location: ") #provide the location to download of the video

#we can predefined the path as well like this
#download_location = "D:\"


pytube.YouTube(video_url).streams.get_highest_resolution().download(download_location)
