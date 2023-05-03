import yt_dlp
import ffmpeg
import os


dir_path = input(
    "Enter Which Folder Do You Want Your Downloaded Youtube Video??\n")
abs_path = os.path.abspath(dir_path)

URLS = input("Enter A Video URL Or Link From Youtube?\n")
with yt_dlp.YoutubeDL() as ydl:
    video_info = ydl.extract_info(URLS, download=False)
    video_title = video_info.get('title', None)
filename = f"{video_title}.mp4"
temp = os.path.join(abs_path, filename)
hello = temp.replace("\\", "/")
location = f"{hello}/"

ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': location,
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'flac',
        'preferredquality': '328',
    }]
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([URLS])
