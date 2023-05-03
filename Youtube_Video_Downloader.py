import yt_dlp
import os


abs_path = os.getcwd()

string = input("Do You Want To Download A playlist??\n")

if string == "Yes" or string == "yes":
    URLS = input("Enter A Playlist URL Or Link From Youtube?\n")
    quality = input("Enter The Quality\n")
    with yt_dlp.YoutubeDL() as ydl:
        playlist_info = ydl.extract_info(URLS, download=False)
        playlist_title = playlist_info.get('title', None)

        for video_info in playlist_info['entries']:
            video_title = video_info.get('title', None)
            filename = f"{video_title}.mp4"
            temp = os.path.join(abs_path, playlist_title, filename)
            hello = temp.replace("\\", "/")
            location = f"{hello}/"

            ydl_opts = {
                'outtmpl': location,
                'format': f'bestvideo[height<={quality[:-1]}][ext=mp4]+bestaudio[ext=m4a]',
                'ignore_config': True,
            }

            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_info['webpage_url']])
else:
    URLS = input("Enter A Video URL Or Link From Youtube?\n")
    quality = input("Enter The Quality\n")
    with yt_dlp.YoutubeDL() as ydl:
        dir_path = input(
            "Enter Which Folder Do You Want Your Downloaded Youtube Video??\n")
        abs_path = os.path.abspath(dir_path)

        video_info = ydl.extract_info(URLS, download=False)
        video_title = video_info.get('title', None)
        filename = f"{video_title}.mp4"
        temp = os.path.join(abs_path, filename)
        hello = temp.replace("\\", "/")
        location = f"{hello}/"
        ydl_opts = {
            'outtmpl': location,
            'format': f'bestvideo[height<={quality[:-1]}][ext=mp4]+bestaudio[ext=m4a]',
            'ignore_config': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download(URLS)
