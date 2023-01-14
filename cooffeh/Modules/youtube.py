from pytube import YouTube
        
def download(text):
    if not text:
        return ''
    video = YouTube(text)
    if not video:
        return ''
    if not video.streams:
        return ''
    resolutions = video.streams.order_by('resolution')
    mp4 = resolutions.filter(file_extension='mp4', progressive="True")
    if len(mp4) == 0:
        return ''
    file_ = './Contents/video.mp4'
    return mp4[len(mp4) - 1].download(file_)
