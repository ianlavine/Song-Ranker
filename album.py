import song

class Album:
    name: str
    score: int
    Songs: [song]

    def __init__(self, name, Songs):
        self.name = name
        self.Songs = Songs
        self.score = 0

    def recalc(self):
        self.score = sum([x.score for x in self.Songs]) / len(self.Songs)

    def __str__(self) -> str:
        """Return a string representation of this tree.
        """
        return (self.name + ": " + str(int(self.score)))

    def __lt__(self, other):
        return self.score > other.score
