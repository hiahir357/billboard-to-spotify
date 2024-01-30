# Billboard to Spotify
# -----------------------------------------------------------------------------------------

import spotipy
from spotipy.oauth2 import SpotifyOAuth
import requests
from bs4 import BeautifulSoup
from utils import is_date_range_valid
from utils import DateFormatException
from utils import final_print
from constants import *

# ------------------------------------
# Setting Spotify authorization
# ------------------------------------
auth_manager = SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    username=USERNAME,
    scope=SCOPE,
    requests_timeout=120,
    show_dialog=True,
)
sp = spotipy.Spotify(auth_manager=auth_manager)
user = sp.current_user()
user_id = user["id"]
# --------------------------------------------------
# Obtaining and validating date from user
# --------------------------------------------------
hot_date = input(
    "Which year do you want to travel to? Type de date in this format YYYY-MM-DD -> "
)
try:
    if not is_date_range_valid(hot_date):
        print("The date range must be between 1955-11-12 and yesterday date")
except DateFormatException as e:
    print(e.message)
# ----------------------------------------------------------------------------------------------------
# Scrap the Billboard's Top 100 according to the date from user input and saving songs and artists
# ----------------------------------------------------------------------------------------------------
hot_by_date = f"{BILLBOARD_HOT_ENDPOINT}/{hot_date}"
response = requests.get(url=hot_by_date)
response.raise_for_status()
result = response.text

soup = BeautifulSoup(result, "html.parser")

song_titles = [
    title.getText().strip("\n\t")
    for title in soup.select(selector=".o-chart-results-list__item h3")
]
song_artists = [
    artist.getText().strip("\n\t")
    for artist in soup.select(selector=".o-chart-results-list__item h3 ~ span")
]
# -----------------------------------
# Obtaning song URIs from Spotify
# -----------------------------------
song_uris = []
year = hot_date.split("-")[0]
for song, artist, index in zip(song_titles, song_artists, range(len(song_titles))):
    print(f"-.{index} Searching {song} from {artist}")

    result = sp.search(
        q=f"track: {song} artist: {artist} year: {year}", type="track", market="VE"
    )

    try:
        found_song = result["tracks"]["items"][0]["name"]
        found_artist = result["tracks"]["items"][0]["artists"][0]["name"]

        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)

        print(f"Found {found_song} from {found_artist}\n")

    except IndexError as e:
        print(f"{song} doesn't exist in Spotify. Skipped.")
# -------------------------
# Creating the playlist
# -------------------------
playlist_creation = sp.user_playlist_create(
    user=user_id, name=f"{hot_date} Billboard 100", public=False
)
playlist_id = playlist_creation["id"]
sp.playlist_add_items(playlist_id=playlist_id, items=song_uris)
final_print()
