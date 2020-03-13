import os
import sys

from save import save_vid, save_audio


def download_audio(links):
	BASE_DIR = os.path.dirname(os.path.abspath(__file__))
	for link in links:
		# save_vid(link, BASE_DIR)
		save_audio(link, BASE_DIR)
	
	
if __name__ == "__main__":
	links = [sys.argv[1],]
	download_audio(links)

