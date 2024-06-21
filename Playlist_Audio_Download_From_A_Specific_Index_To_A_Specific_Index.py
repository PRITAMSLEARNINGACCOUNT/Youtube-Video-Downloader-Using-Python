import yt_dlp
import os
abs_path = os.getcwd()
playlist_url = input("Enter A Playlist URL Or Link From Youtube?\n")
start_index = int(input(
    "Enter Where Do You Want To Start Downloading Audios From A Playlist?\n"))
end_index = int(
    input("Enter Where Or To Which Video Do You Want To Stop Downloading??\n"))
keep = input("Where Do You Want To Keep Downloaded Audios?\n")
with yt_dlp.YoutubeDL() as ydl:
    temp = abs_path.replace("\\", "/")
    location = f"{temp}/{keep}/"
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': location + '%(title)s.%(ext)s',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'flac',
            'preferredquality': '328',
        }],
        'playliststart': start_index,
        'playlistend': end_index,

    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print(ydl.download([playlist_url]))
