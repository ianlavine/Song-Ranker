from scrape import scrape_data
from artist import Artist
from album import Album

names = ["Car Seat Headrest", "Kanye", "Flume"]

def return_artists():
    artists = []
    for name in names:
        data = scrape_data(name)
        albums = []
        for content in data:
            albums.append(Album(content[1], content[0]))
        artists.append(Artist(name, albums))
        albums.clear()

    return artists

# return_artists()