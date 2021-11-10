import random
import math

def coolmath():
    x = random.randint(0, 100)
    if x < 21:  # 21
        return 1
    elif x < 39:  # 18
        return 2
    elif x < 54:  # 15
        return 3
    elif x < 67:  # 13
        return 4
    elif x < 78:  # 11
        return 5
    elif x < 87:  # 9
        return 6
    elif x < 94:  # 7
        return 7
    else:  # 6
        return 8

def new_battle(Songs):
    choice = random.randint(0, len(Songs) - 1)
    updown = random.randint(0, 1)
    if updown == 1:
        offby = abs(choice - coolmath())
    else:
        offby = choice + coolmath()
        if offby > len(Songs) - 1:
            offby = offby - (offby - (len(Songs) - 1))
    Song1 = Songs[choice]
    Song2 = Songs[offby]
    return [Song1, Song2]

def compare(winner, loser):
    ratio = 50 + int(50 * (winner.score  - loser.score) / max(winner.score, loser.score))
    win = winner.score
    lose = loser.score

    winner.score += 250 * (1.0 / (1.0 + (math.pow(10, (win - lose) / 400))))
    loser.score -= 250 * (1.0 / (1.0 + (math.pow(10, (win - lose) / 400))))