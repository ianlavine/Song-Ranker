from song import Song

class Album:
    name: str
    score: int
    Songs: list[Song]

    def __init__(self, name, Songs):
        self.name = name
        self.Songs = Songs
        self.score = 0

    def recalc(self):
        self.score = sum([x.score[0] for x in self.Songs]) / len(self.Songs)

    def reset(self):
        for song in self.Songs:
            song.score == 1000

    def __str__(self) -> str:
        """Return a string representation of this album.
        """
        return (self.name + ": " + str(int(self.score)))

    def __lt__(self, other):
        return self.score > other.score
