import requests
from bs4 import BeautifulSoup
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint

# CLIENT_ID = os.environ.get("CLIENT_ID")
# CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
CLIENT_ID = "37611e0ae562432daba7c5d6764cd257"
CLIENT_SECRET = "6708b163b3ca4e6ab613f04c967dbcbf"
URI = "http://example.com"

scope = "playlist-modify-private"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    scope=scope,
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=URI,
    show_dialog=True,
    cache_path="token.txt"))

user_id = sp.current_user()["id"]

# Ask user what year they would like to travel to
travel_date = input("Which year do you want to travel to? Type the date in the format YYYY-MM-DD: ")
# travel_date = "2020-04-20"
year = travel_date[0:4]

# Get the HTML code from the Billboard website
# print(f"https://www.billboard.com/charts/hot-100/{travel_date}")
response = requests.get(f"https://www.billboard.com/charts/hot-100/{travel_date}")
songs_webpage = response.text

# Make beautiful soup object and find song titles and ranking of Billboard Hot 100
soup = BeautifulSoup(songs_webpage, "html.parser")
song_title_tags = soup.select(selector="li h3#title-of-a-story")
song_titles = [song.getText().strip() for song in song_title_tags]

# Create list of Spotify song URIs for the hot 100 songs
# song_uris = [f"spotify:track:{song} year:{year}" for song in song_titles]
song_uris = []
for song in song_titles:
    result = sp.search(q=f"track:{song} year:{year}", type="track", limit=1)
    # print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# pprint(song_uris)
# print(type(song_uris))
# print(len(song_uris))
# print(song_uris)

# Create Spotify playlist
playlist = sp.user_playlist_create(user=user_id, name=f"{travel_date} Billboard 100", public=False)
playlist_id = playlist["id"]
print(playlist_id)

sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)
