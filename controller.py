import os

from save import save_vid, save_audio


def download_audio(links):
	BASE_DIR = os.path.dirname(os.path.abspath(__file__))
	for link in links:
		# save_vid(link, BASE_DIR)
		save_audio(link, BASE_DIR)
	
	
if __name__ == "__main__":
	links = [
		"https://www.youtube.com/watch?v=uX3IZ80dXsU", 
		"https://www.youtube.com/watch?v=q6cDn9sMRME", 
		"https://www.youtube.com/watch?v=1w_uufUG9Ac",
		"https://www.youtube.com/watch?v=22lhyM5zMHQ",
		"https://www.youtube.com/watch?v=84nwUEIMQr8",
		"https://www.youtube.com/watch?v=ekgPDRTyriY",
		"https://www.youtube.com/watch?v=sPy5ospxyPE",
		"https://www.youtube.com/watch?v=jPCLhSseIb8",
		"https://www.youtube.com/watch?v=sSts_WOEE-s",
	]
	download_audio(links)

