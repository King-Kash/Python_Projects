from pytube import YouTube
from sys import argv

#argv[0] is always the name of the program and then argv[1] will be the link
link = "https://www.youtube.com/watch?v=vEQ8CXFWLZU"
yt = YouTube(link)

print("title: ", yt.title)
print("views: ", yt.views)


