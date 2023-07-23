# import pytube
#
# # Youtube video URL
# link = "https://www.youtube.com/watch?v=0ihA1jxyvvM&t=396s"
# yt = pytube.YouTube(link)
#
# print("Title:", yt.title)
# print("Author:", yt.author)
# print("Published date:", yt.publish_date.strftime("%Y-%m-%d"))
# print("Number of views:", yt.views)
# print("Length of video:", yt.length, "seconds")
#
# yt.streams.get_highest_resolution().download()
# print("Video successfullly downloaded from", link)


from pytube import YouTube
YouTube('https://www.youtube.com/watch?v=0ihA1jxyvvM').streams.first().download()
