import pprint

from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth, SpotifyClientCredentials

spotify_id = "9d9ad2df6b73452f961f7494276a5c0d"
spotify_secret = "ec714743c6ad4658b724be43d2d27bf0"
client_cred = SpotifyClientCredentials(client_id=spotify_id, client_secret=spotify_secret)

date = input("yyyy-dd-mm:")
top_100 = requests.get(f"https://www.billboard.com/charts/hot-100/{date}/")
top_100_txt = top_100.text

soup = BeautifulSoup(top_100_txt, "html.parser")
selector = soup.select(selector="li ul li h3")
#print(selector)
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spotify_id,client_secret=spotify_secret,
                                               redirect_uri="https://example.com/",
                                               username="dread_ford",
                                               scope="playlist-modify-private",
                                               show_dialog="true",
                                               cache_path="token,txt",
                                               ))
user = sp.current_user()
print(user["id"])

year = date.split("-")[0]
#print(year)

song_urls = []
for song in selector:
    songs = song.getText()
    results = sp.search(q=f"track:{songs}"f"year:{year}", type="track",)
    #print(songs)
    try:
        uri = results["tracks"]["items"][0]["uri"]
        append = song_urls.append(uri)
        #print(uri)
    except IndexError:
        print("song not found skipped")
pprint.pp(song_urls)
created_playlist = sp.user_playlist_create(user=user["id"], name=f"{date} playlist", public=False, description="A playlist for a timr in history")
add_songs = sp.playlist_add_items(playlist_id=created_playlist["id"], items=song_urls,)

