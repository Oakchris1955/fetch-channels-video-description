#import modules
import scrapetube, yt_dlp, time, json

#get channel ID
channel_id = str(input('Enter the channel ID you wanna fetch: '))

#get channel videos
videos = scrapetube.get_channel(channel_id)

#define some variables
videos_id_list = description_list = []


try:
	#loop through the vids and append their IDs to a list
	for video in videos:
		#print(video['videoId'])
		videos_id_list.append(video['videoId'])
except json.JSONDecodeError:
	#if invalid channel ID is given, exit
	print('Please enter a valid channel ID')
	quit()

print('Fetched channel\'s videos')

i = 0

#loop thruough the video IDs
for video_id in videos_id_list:
	youtube_dlp_options = {
		'skip_download': True,
		'ignoreerrors': True
	}
	with yt_dlp.YoutubeDL(youtube_dlp_options) as ydl:
		#gte video info
		video_info = ydl.extract_info(video_id)
		#get video description
		video_description = video_info['description']
		#append description to list
		description_list.append(video_description)
		#wait for 100ms so that YouTube doesn't block us for too many requests
		time.sleep(0.1)
		i+=1
		print(f'Downloaded {i} video(s) out of {len(videos_id_list)}')

print('Finished downloading videos')

#save the descriptions list in a json file
with open('descriptions.json', 'w') as f:
	json.dump({f'{channel_id}' : description_list}, f)