from pytube import YouTube
from sys import argv

#argv[0] is always the name of the program and then argv[1] will be the link
link = argv[1]
yt = YouTube(link)

print("title: ", yt.title)
print("views: ", yt.views)
yd = yt.streams.get_highest_resolution()
yd.download('/Users/kashyapkanumuri/Downloads/YouTube-Downloads')


