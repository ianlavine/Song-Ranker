import math

class Song:
    # score: dict
    score: float
    name: str

    def __init__(self, name: str = '', score=1000.0):
        self.score = score
        self.name = name

    def __str__(self) -> str:
        """Return a string representation of this song."""
        return self.name + ": " + str(int(self.score))

    def fight(self, other, vict: bool):
        self.matches += 1
        if vict:
            self.score += 250 * (
                        1.0 / (1.0 + (math.pow(10, (self.score - other.score) / 400))))
        else:
            self.score -= 250 * (
                        1.0 / (1.0 + (math.pow(10, (other.score - self.score) / 400))))

    def __lt__(self, other):
        return self.score > other.score
