import moviepy.editor as mp
import os
import shutil

from pytube3save1video import save_vid


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
save_vid(BASE_DIR)

title = os.listdir(os.path.join(BASE_DIR, "video\\"))[0]
with mp.VideoFileClip(os.path.join(BASE_DIR, "video\\{}".format(title))) as clip:
	clip.audio.write_audiofile(os.path.join(BASE_DIR, "audios\\{}.mp3").format(title.replace('.mp4', '')))

print("deleting placeholder dir")
shutil.rmtree(os.path.join(BASE_DIR, "video"))
