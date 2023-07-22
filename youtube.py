from pytube import YouTube

link=input("Enter link: ")
yt=YouTube(link)

print("choose 'audio' or 'video'")
option=input("Enter choice: ")

print(yt.title)
print(yt.thumbnail_url)

print("Downloading...")
def saveaudio():
    audio=yt.streams
    audio.get_audio_only().download()

def savevideo():
    video=yt.streams.get_lowest_resolution()
    video.download()

if(option=="audio"):
    saveaudio()
if(option=="video"):
    savevideo()

print("Download completed")



