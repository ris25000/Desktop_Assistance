from googleapiclient.discovery import build

def get_youtube_video_link(video_name, api_key):
# Searches for a video on YouTube based on the provided video name and returns the URL of the first search result.
# Args:video_name (str): The name of the video to search for.
# api_key (str): The YouTube Data API key for authentication.
# Returns:str or None: The URL of the first search result if found, else None."""
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