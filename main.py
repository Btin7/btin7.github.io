#made by Btn

import yt_dlp as youtube_dl

# Get the youtube video link
url = input("Enter your YouTube link here: ")

# Download options
ydl_opts = {}

# Ask the user for the file format (mp3 or mp4)
file_format = input("Please enter your file format (mp3/mp4): ").lower()

if file_format == "mp3":
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("Downloaded and converted to MP3.")

elif file_format == "mp4":
    ydl_opts = {
        'format': 'bestvideo+bestaudio',
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
    print("Downloaded MP4 video.")

else:
    print("Invalid file format selected. mp3 and mp4 only.")
