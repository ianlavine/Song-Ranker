from album import Album

class Artist:
    name: str
    Albums: Dict[Album: bool]

    def __init__(self, name, Albums):
        self.name = name
        self.Albums = Albums
        self.Album_dict = {x: True for x in Albums}

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

