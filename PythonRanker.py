import random
import math
from song import Song
from album import Album
from artist import Artist
import user_data

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
    artist: Artist
    songs: list[Song]
    albums: list[Album]

    def __init__(self, a):

        self.artist = a
        self.Songs = []
        self.Albums = []

        self.instantiate_albums()

        # self.runsim()

    def instantiate_albums(self):

        self.Albums.clear()
        self.Songs.clear()

        for album in self.artist.Albums:
            if self.artist.Album_dict[album]:
                for song in album.Songs:
                    self.Songs.append(song)
                self.Albums.append(album)


    def edit_albums(self):
        while True:
            albs = [str(x.name) + ": " +  str(self.artist.Album_dict[x]) for x in self.artist.Albums]
            albs.append((100, "Done"))
            removal = options("Which albums would you like/not like to include: ", albs)
            if removal == 100:
                self.instantiate_albums()
                break
            else:
                self.artist.swap(self.Albums[removal - 1])


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


    def showstats(self):
        self.Songs.sort()
        for x in range(10):
            print(str(x + 1) + ". " + str(self.Songs[x]))

    def showSongStats(self):
        self.Songs.sort()
        topten = [self.Songs[x] for x in range(10)]
        return topten

    def showAlbumstats(self):
        for album in self.Albums:
            album.recalc()
        self.Albums.sort()
        for x in range(len(self.Albums)):
            print(str(x + 1) + ". " + str(self.Albums[x]))


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

            match += 1
            response = options('\n' + str(match), (Song1.name, Song2.name, (0, "Quit")))
            if response == 1:
                self.compare(Song1, Song2)
            elif response == 2:
                self.compare(Song2, Song1)
            elif response == 0:
                leave = True

    def new_battle(self):
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
        return [Song1, Song2]

    def compare(self, winner, loser):
        ratio = 50 + int(50 * (winner.score[user] - loser.score[user]) / max(winner.score[user], loser.score[user]))
        win = winner.score[user]
        lose = loser.score[user]

        winner.score[user] += 250 * (1.0 / (1.0 + (math.pow(10, (win - lose) / 400))))
        loser.score[user] -= 250 * (1.0 / (1.0 + (math.pow(10, (win - lose) / 400))))

    def runsim(self):
        while True:
            response = options(None, ["Play", "Different Artist", "Edit Artist", "Stats"])
            if response == 1:
                self.Songs.sort()
                self.battle()
            elif response == 2:
                main()
                break
            elif response == 3:
                self.edit_albums()
            elif response == 4:
                self.showstats()
                self.showAlbumstats()

# artists = user_data.return_artists(None)

# def main():
#     opt = [a for a in artists]
#     opt.append((100, "Choose a new artist"))
#     opt.append((0, "Quit"))
#     choice = options("Welcome\nChoose An Artist!", opt)
#     if choice == 100:
#         art = input("Who: ")
#         artists.extend(user_data.return_artists([art]))
#         main()
#     elif choice == 0:
#         pass
#     else:
#         Play(artists[choice - 1])
#     return choice

# def options(main_text, options):
#     dict_options = create_options(options)
#     return display_options(main_text, dict_options)

# def create_options(text):
#     text_dict = dict()
#     counter = 1
#     for i in text:
#         if not isinstance(i, tuple):
#             text_dict[counter] = i
#             counter += 1
#         else:
#             text_dict[i[0]] = i[1]
#     return text_dict

# def display_options(main_text, text):
#     if main_text is None:
#         main_text = "What would you like to do?"
#     print(main_text + "\n")
#     while(True):
#         for option in text:
#             print(str(option) + ": " + str(text[option]))
#         choice = input()
#         if choice.isnumeric() and int(choice) in text.keys():
#             return int(choice)
#         print("\ninvalid choice")

# main()

