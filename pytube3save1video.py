from pytube import YouTube
import moviepy.editor as mp
import os
import shutil


def save_vid(dir):
	yt = YouTube("https://www.youtube.com/watch?v=zQA-vg43H48")
	stream = yt.streams.first()
	stream.download(os.path.join(dir, "video"))
