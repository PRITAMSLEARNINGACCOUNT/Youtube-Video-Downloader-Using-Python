import yt_dlp
import os
abs_path = os.getcwd()
playlist_url = input("Enter A Playlist URL Or Link From Youtube?\n")
quality = input("Enter The Quality\n")
start_index = int(input(
    "Enter Where Do You Want To Start Downloading Videos From A Playlist?\n"))
end_index = int(
    input("Enter Where Or To Which Video Do You Want To Stop Downloading??\n"))
keep = input("Where Do You Want To Keep Downloaded Videos?\n")
with yt_dlp.YoutubeDL() as ydl:
    temp = abs_path.replace("\\", "/")
    location = f"{temp}/{keep}/"
    ydl_opts = {
        'format': f'bestvideo[height<={quality[:-1]}][ext=mp4]+bestaudio[ext=m4a]',
        'outtmpl': location + '%(title)s.%(ext)s',
        'playliststart': start_index,
        'playlistend': end_index,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])
