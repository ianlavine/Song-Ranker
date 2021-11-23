import requests
import base64
import datetime
from urllib.parse import urlencode

client_id = '7156102a1f8f4e5a968516a088eca42d'
client_secret = 'cef76e2e8f884826b7a447e82fca3800'

class SpotifyAPI(object):
    access_token = None
    access_token_expires = datetime.datetime.now()
    access_token_did_expire = datetime.datetime.now()
    client_id = None
    client_secret = None
    token_url = 'https://accounts.spotify.com/api/token'

    def __init__(self, client_id, client_secret, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.client_id = client_id
        self.client_secret = client_secret

    def get_token_header(self):
        client_creds = f"{self.client_id}:{self.client_secret}"
        client_creds_bs4 = base64.b64encode(client_creds.encode())
        return {
            "Authorization" : f"Basic {client_creds_bs4.decode()}",
            "Content-Type" : 'application/x-www-form-urlencoded'
            }

    def get_token_data(self):
        return { 'grant_type' : 'client_credentials' }

    def perform_auth(self):
        token_data = self.get_token_data()
        token_headers = self.get_token_header()
        r = requests.post(self.token_url, data=token_data, headers=token_headers)

        if r.status_code not in range(200, 299):
            return False
        
        data = r.json()
        now = datetime.datetime.now()
        self.access_token = data['access_token']
        expires_in = data['expires_in']
        self.access_token_expires = now + datetime.timedelta(seconds=expires_in)
        self.access_token_did_expire = self.access_token_expires < now

        return True

class Artist():

    header = None
    search = None
    artist = None
    albums = {}
    songs = []
    artist_id = None

    def __init__(self, search):
        self.headers = self.create_headers()
        self.search = search

    def create_headers(self):
        spotify = SpotifyAPI(client_id, client_secret)
        spotify.perform_auth()

        access_token = spotify.access_token
        return {
            "Authorization" : f"Bearer {access_token}"
        }

    def get_artist(self):

        art_endpoint = "	https://api.spotify.com/v1/search"

        data = urlencode({"q" : str(self.search), "type": "artist"})
        lookup_url = f"{art_endpoint}?{data}"

        r = requests.get(lookup_url, headers=self.headers)
        art_choice = r.json()['artists']['items'][0]
        self.artist_id = art_choice['id']
        self.artist = art_choice['name']

    def get_albums(self):
        alb_endpoint = f"   https://api.spotify.com/v1/artists/{self.artist_id}/albums"
        data = urlencode({"include_groups": "album"})
        lookup_url = f"{alb_endpoint}?{data}"

        r2 = requests.get(lookup_url, headers=self.headers)
        alb_choices = r2.json()['items']
        self.albums = {x['name']: [x['id'], x['images'][0]['url']] for x in alb_choices}
        print(self.albums)

    def get_songs(self):
        for alb in self.albums:

            song_endpoint = f"	https://api.spotify.com/v1/albums/{self.albums[alb][0]}/tracks"
            r3 = requests.get(song_endpoint, headers=self.headers)
            song_choices = r3.json()['items']
            songs = [x['name'] for x in song_choices]
            self.albums[alb].append(songs)

    def execute_order(self):
        self.get_artist()
        self.get_albums()
        self.get_songs()
        return (self.artist, self.albums)


def scrape_data(a):
    artist = Artist(a)
    return artist.execute_order()

    
scrape_data("black country, new roads")