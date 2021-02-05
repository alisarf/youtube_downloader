import pytube

print("Welcome to the YouTube Downloader.")
      
url = input("Enter YouTube Url: ")

video = pytube.YouTube(url)

stream = video.streams.get_by_itag(22)
print("Downloading...")

stream.download(filename= 'your_requested_video')

print("Done")
