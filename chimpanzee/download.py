from moviepy.editor import *
import moviepy

name = 'ChimpVid'
video = VideoFileClip(f'{name}.mp4').subclip(18.4,21.4)
video.write_videofile(f'{name}_clipped.mp4',fps=60)