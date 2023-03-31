# from moviepy.editor import *
#
# def transToFlac:
#
#     # Load the video file
#     video = VideoFileClip("/Users/wilburwong/Downloads/input.mkv")
#
#     # Extract the audio track
#     audio = video.audio
#
#     # Save the audio track as a FLAC file
#     audio.write_audiofile("output.flac", codec="flac")
#
# from pydub import AudioSegment
#
# def editFlac:
#     # Load the audio file
#     audio = AudioSegment.from_file("output.flac", format="flac")
#
#     # Define the start and end times of the segment to keep
#     start_time = 43000  # in milliseconds
#     end_time = 659000  # in milliseconds
#
#     # Extract the segment between the specified time range
#     segment = audio[start_time:end_time]
#
#     # Save the segment as a new FLAC filed
#     segment.export("edited_output.flac", format="flac")

from pydub import AudioSegment

# Load the edited FLAC file
audio = AudioSegment.from_file("edited_output.flac", format="flac")

# Define the output file name and format
output_file = "output.mp3"

# Export the audio as MP3 format
audio.export(output_file, format="mp3")

