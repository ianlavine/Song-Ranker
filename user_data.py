import spotify
from entities import album, artist, song

names = []

def return_artists(art):
    if art == None:
        art = names
    artists = []
    for name in art:
        data = spotify.scrape_data(name)
        albums = []
        for content in data[1]:
            song_content = []
            for s in data[1][content][2]:
                song_content.append(song.Song(s))
            albums.append(album.Album(content, song_content, data[1][content][1]))
        artists.append(artist.Artist(name, albums))

    return artists

