import scrape
from entities import album, artist, song

names = []

def return_artists(art):
    if art == None:
        art = names
    artists = []
    for name in art:
        data = scrape.scrape_data(name)
        albums = []
        for content in data:
            song_content = []
            for s in content[0]:
                song_content.append(song.Song(s))
            albums.append(album.Album(content[1], song_content))
        artists.append(artist.Artist(name, albums))

    return artists

