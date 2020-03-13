from pytube import YouTube
import os


def save_vid(video_link, dir):
	# yt = YouTube("https://www.youtube.com/watch?v=zQA-vg43H48")
	yt = YouTube(video_link)
	stream = yt.streams.first()
	stream.download(os.path.join(dir, "video"))
	
	
def save_audio(video_link, dir):
	yt = YouTube(video_link)
	title = yt.title
	while(title == "YouTube"):
		yt = YouTube(video_link)
		title = yt.title
	print("Now downloading '{}".format(title))
	audio = yt.streams.get_audio_only()
	audio.download(os.path.join(dir, "audio_only"))
	print("Download complete. Enjoy your new music(:")
	

if __name__ == "__main__":
	save_audio("https://www.youtube.com/watch?v=uX3IZ80dXsU", "")
