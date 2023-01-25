from pytube import YouTube
from Models.Audio import Audio
from Shared import tools

def getVideo(text):
    streams = YouTube(text).streams
    mp4 = streams.order_by('resolution').filter(
        file_extension='mp4', progressive="True")
    return mp4.last().download('Contents',f'{tools.fileName()}.mp4')

def getAudio(text):
    yt = YouTube(text)
    audio = Audio()
    audio.title = yt.title
    audio.author = yt.author
    audio.thumb = yt.thumbnail_url
    audio.duration = yt.length
    mp3 = yt.streams.filter(only_audio=True).last()
    audio.file_ = mp3.download('Contents',f'{tools.fileName()}.mp3')
    return audio