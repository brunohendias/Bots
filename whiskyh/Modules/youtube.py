from pytube import YouTube as yt

class Youtube():
    def downloadVideo(self, msg):
        streams = yt(msg.text).streams.order_by('resolution').filter(
            file_extension='mp4', progressive="True")
        if not streams:
            return ''
        output_path = './Contents/'
        filename = "video.mp4"
        return streams[len(streams) - 1].download(output_path, filename)
