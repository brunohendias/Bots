from pytube import YouTube
        
def download(text):
    streams = YouTube(text).streams
    mp4 = streams.order_by('resolution').filter(
        file_extension='mp4', progressive="True")
    return mp4.last().download('Contents','video.mp4')
