#pip install pytube
from pytube import YouTube

link = input("Enter url link: ")

video = YouTube(link)

stream = video.streams.get_highest_resolution()

stream.download()
