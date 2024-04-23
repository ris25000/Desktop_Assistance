from googleapiclient.discovery import build

def get_youtube_video_link(video_name, api_key):
    youtube = build('youtube', 'v3', developerKey=api_key)

    # Search for videos with the given name
    search_response = youtube.search().list(
        q=video_name,
        part='id',
        maxResults=1,
        type='video'
    ).execute()

    # Extract video ID1
    if 'items' in search_response and len(search_response['items']) > 0:
        video_id = search_response['items'][0]['id']['videoId']
        return f'https://www.youtube.com/watch?v={video_id}'
    else:
   
        return None