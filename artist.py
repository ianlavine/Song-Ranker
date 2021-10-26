from album import Album

class Artist:
    name: str
    Album_dict: dict[Album: bool]
    Albums: list[Album]

    def __init__(self, name, albums):
        self.name = name
        self.Albums = albums
        self.Album_dict = {x: True for x in albums}

    def get_albums(self):
        return [x for x in self.Albums if self.Album_dict[x]]

    def reset_album(self, album):
        if album in self.Albums:
            album.reset()

    def full_reset(self):
        for album in self.Albums:
            self.reset_album(album)

    def swap(self, album):
        if album in self.Albums:
            self.Album_dict[album] = not self.Album_dict[album]

    def __str__(self) -> str:
        """Return a string representation of this artist.
        """
        return (self.name)

