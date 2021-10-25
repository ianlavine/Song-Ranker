import random
import math
import sys
from scrape import scrape_data
from song import Song
from album import Album
from artist import Artist

user = 0
match = 0

# file = open("Values.txt", "r")
# values = file.readlines()
# file.close()
# songs = [()]
# for i in range(0, len(songs)):
#     songs.append(Song(songs[i]))
    # self.Songs.append(Song(values[i].strip('\n'), float(values[i + 1]), int(values[i + 2])))

class Play:
    Artists: list[Artist]
    Songs: list[Song]
    Albums: list[Album]

    def __init__(self):

        data = scrape_data(artist)

        self.Songs = []
        self.albums = []

        for pairing in data:
            alb_songs = []
            for song in pairing[0]:
                alb_songs.append(Song(song))
            self.albums.append(Album(pairing[1], alb_songs))

        self.remove_albums()

        for album in self.albums:
            self.Songs.extend(album.Songs)

        self.runsim()

    def remove_albums(self):
            removal = 0
            while True:
                for i in range(0, len(self.albums)):
                    print(str(i) + ". " + self.albums[i].name)
                removal = int(input("Which albums would you not like to include: "))
                if removal == 100:
                    break
                self.albums.pop(removal)


    def coolmath(self):
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


    def user_compare(self):
        print('Which users are being compared?')
        v1 = users[input("user 1:")]
        v2 = users[input("user 2:")]

        # total_dif = 0
        # indiv_dif = []
        # for Song in self.Songs:
        #     dif = abs(Song.score[v1] - Song.score[v2])
        #     total_dif += dif
        #     indiv_dif.append((Song.name, dif))
        #
        # deci = 100 * (1 - total_dif / (len(self.Songs) * 1000))

        global user
        user = v1
        self.Songs.sort()
        ranks = {self.Songs[i].name: i for i in range(0, len(self.Songs))}
        user = v2
        self.Songs.sort()
        total_dif = 0
        indiv_dif = []
        for i in range(0, len(self.Songs)):
            print(i)
            print(ranks[self.Songs[i].name])
            dif = abs(i - ranks[self.Songs[i].name])
            total_dif += dif
            indiv_dif.append((self.Songs[i].name, dif))

        deci = 100 * (1 - total_dif / (len(self.Songs)**2 / 2))

        indiv_dif.sort(key=lambda x: x[1], reverse=True)

        print("Differences in position:")
        for x in indiv_dif:
            print(x[0] + ": " + str(x[1]))

        print("\n these users have " + str(deci) + "% similarity")


    def compare(self, winner, loser):
        ratio = 50 + int(50 * (winner.score[user] - loser.score[user]) / max(winner.score[user], loser.score[user]))
        print('expected at: ' + str(ratio))
        win = winner.score[user]
        lose = loser.score[user]

        winner.score[user] += 250 * (1.0 / (1.0 + (math.pow(10, (win - lose) / 400))))
        loser.score[user] -= 250 * (1.0 / (1.0 + (math.pow(10, (win - lose) / 400))))


    def showstats(self):
        for x in range(len(self.Songs)):
            print(str(x + 1) + ". " + str(self.Songs[x]))


    def tournament(self, Songs=None, losers=None, n=0):

        if self.Songs is None:
            self.Songs = Songs
            losers = []

        if len(self.Songs) == 1:
            for i in losers:
                for j in i:
                    sys.stdout.write(j.name + ", ")
                    sys.stdout.flush()
                print('\n')
            print(self.Songs[0])
        else:
            random.shuffle(self.Songs)
            remaining = []
            addition = []
            for Song in range(0, len(self.Songs), 2):
                print('\n' + str(n))
                print('1. ' + self.Songs[Song].name)
                print('2. ' + self.Songs[Song + 1].name)
                response = input("choose: ")

                if response.isnumeric() and int(response) < 3:
                    if response == '1':
                        remaining.append(self.Songs[Song])
                        addition.append(self.Songs[Song + 1])
                    elif response == '2':
                        remaining.append(self.Songs[Song + 1])
                        addition.append(self.Songs[Song])
            losers.append(addition)
            self.tournament(remaining, losers, n + 1)


    def battle(self):

        global match
        leave = False
        while not leave:
            choice = random.randint(0, len(self.Songs) - 1)
            updown = random.randint(0, 1)
            if updown == 1:
                offby = abs(choice - self.coolmath())
            else:
                offby = choice + self.coolmath()
                if offby > len(self.Songs) - 1:
                    offby = offby - (offby - (len(self.Songs) - 1))
            Song1 = self.Songs[choice]
            Song2 = self.Songs[offby]

            move_on = False
            match += 1
            while not move_on:
                print('\n' + str(match))
                print('1. ' + Song1.name)
                print('2. ' + Song2.name)
                response = input("choose: ")

                if response.isnumeric() and 0 < int(response) < 3:
                    if response == '1':
                        self.compare(Song1, Song2)
                    elif response == '2':
                        self.compare(Song2, Song1)
                    self.Songs.sort()
                    move_on = True
                elif response == '3':
                    move_on = True
                    leave = True

    def endsim(self):
        file = open("Values.txt", "w")
        for Song in self.Songs:
            file.write('%s\n' % str(Song.name))
            file.write('%s\n' % str(Song.score))
            file.write('%s\n' % str(Song.matches))
        file.close()

    def runsim(self):
        run = True
        while run:
            print('1. Battle Mode')
            print('2. Tournament')
            print('3. Stats')
            print('4. Quit')
            print('5. Compare User')
            response = input("choose: ")
            if response == '1':
                self.Songs.sort()
                self.battle()
            elif response == '2':
                self.tournament()
            elif response == '3':
                self.showstats()
            elif response == '4':
                self.endsim()
                run = False
            elif response == '5':
                self.user_compare()


def showAlbumstats(Albums):
    for album in Albums:
        album.recalc()
    Albums.sort()
    for x in range(len(Albums)):
        print(str(x + 1) + ". " + str(Albums[x]))


artist = input("choose an artist: ")
play = Play()
