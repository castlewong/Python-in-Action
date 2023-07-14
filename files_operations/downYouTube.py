from pytube import YouTube

video_url = "https://www.youtube.com/watch?v=0ihA1jxyvvM"

yt = YouTube(video_url)

stream = yt.streams.get_highest_resolution()

output_path = "/youtube"

stream.download(output_path)