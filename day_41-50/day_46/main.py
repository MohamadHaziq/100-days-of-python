import requests
import json
import spotipy
import json
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup

with open('./day_41-50/day_46/creds.json') as file:
    creds = json.load(file)

date_to_scrape = input("What is the date to scrape? YYYY-MM-DD format:\n")

url_to_scrape = f"https://www.billboard.com/charts/hot-100/{date_to_scrape}"

response = requests.get(url=url_to_scrape)
soup = BeautifulSoup(response.text, "html.parser")

extract = soup.find_all('span', class_ = "chart-element__information__song")
song_list = [song.text for song in extract]

extract = soup.find_all('span', class_ = "chart-element__information__artist")
artist_list = [artist.text for artist in extract]

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://localhost",
        client_id=creds['client_id'],
        client_secret=creds['client_secret'],
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

year = date_to_scrape.split('-')[0]

song_uri = []

for song in song_list:
    result = sp.search(q= f"track:{song} year:{year}", type = "track")
    try:
        uri = result['tracks']['items'][0]["uri"]
        song_uri.append(uri)
    except IndexError:
        print (f"{song} does not exist in Spotify. Skipped")

playlist = sp.user_playlist_create(user_id, f"{date_to_scrape} Billboard Top 100", description="My attempt at creating playlists programatically", public=False)

sp.user_playlist_add_tracks(user_id, playlist['id'], song_uri)