import requests

API_KEY = "AIzaSyAKROCKnHs21WLfAll2CbwJBmjCmHnEPCg"
SEARCH_QUERY = "python django tutorial"

url = "https://www.googleapis.com/youtube/v3/search"

params = {
    "part": "snippet",
    "q": SEARCH_QUERY,
    "type": "video",
    "maxResults": 15,
    "key": API_KEY
}

response = requests.get(url, params=params)
data = response.json()

for item in data["items"]:
    title = item["snippet"]["title"]
    video_id = item["id"]["videoId"]
    print(f"Title: {title}")
    print(f"Link: https://www.youtube.com/watch?v={video_id}")
    print("-" * 50)