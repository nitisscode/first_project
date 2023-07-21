from pytube import YouTube

link=input("Enter link: ")
yt=YouTube(link)

print(yt.title)
print(yt.thumbnail_url)

print("Downloading...")

audio=yt.streams
audio.get_audio_only().download()

video=yt.streams.get_lowest_resolution()
video.download()

print("Download completed")



