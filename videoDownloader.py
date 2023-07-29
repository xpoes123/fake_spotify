from __future__ import unicode_literals
import yt_dlp
import os

def download(url, name):
    destination = "./songs/"
    ydl_opts = {
        'outtmpl': './songs/1.%(ext)s',
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'wav',
        }],
    }

    def download_from_url(url):
        ydl.download([url])
        os.rename(destination +"1.wav", destination+name.replace(" ", "_")+".wav")

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # url=input("Enter Youtube URL: ")
        download_from_url(url)
