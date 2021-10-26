import math

user = 0

class Song:
    # score: dict
    score: list
    matches: int
    name: str

    def __init__(self, name: str = '', score=1000.0, matches: int = 0):
        self.score = [score, score, score]
        self.matches = matches
        self.name = name

    def __str__(self) -> str:
        """Return a string representation of this song."""
        return self.name + ": " + str(int(self.score[user]))

    def fight(self, other, vict: bool):
        self.matches += 1
        if vict:
            self.score += 250 * (
                        1.0 / (1.0 + (math.pow(10, (self.score[user] - other.score[user]) / 400))))
        else:
            self.score -= 250 * (
                        1.0 / (1.0 + (math.pow(10, (other.score[user] - self.score[user]) / 400))))

    def __lt__(self, other):
        return self.score[user] > other.score[user]
