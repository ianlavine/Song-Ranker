from scrape import scrape_data
from artist import Artist
from album import Album
from song import Song

names = ["Flume"]

def return_artists(art):
    if art == None:
        art = names
    artists = []
    for name in art:
        data = scrape_data(name)
        albums = []
        for content in data:
            song_content = []
            for s in content[0]:
                song_content.append(Song(s))
            albums.append(Album(content[1], song_content))
        artists.append(Artist(name, albums))

    return artists

# return_artists(None)