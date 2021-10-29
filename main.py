from flask import Flask, request, render_template
import user_data
import PythonRanker

app = Flask(__name__)

artists = user_data.return_artists(None)
artist_data = [{'name': artists[x].name, 'val': str(x)} for x in range(len(artists))]
game = None
game_songs = None
album_data = []
song_data = []
topten = []

@app.route("/")
def index():

    global game, game_songs, album_data, song_data, topten

    choice = request.args.get("chosen_artist", "")
    if choice:
        artist = artists[int(choice)]
        album_data = get_albums(artist)
        game = PythonRanker.Play(artist)
        song_data, game_songs = new_song(game)

    song_choice = request.args.get("chosen_song", "")
    if song_choice:
        if song_choice == 0:
            game.compare(game_songs[0], game_songs[1])
        else:
            game.compare(game_songs[1], game_songs[0])
        song_data, game_songs  = new_song(game)
        topten = top_ten(game)

    return render_template('index.html', artist_data=artist_data, album_data=album_data, song_data=song_data, topten=topten)


def choose_artist(artist):
    for art in artists:
        if artist == art.name:
            return art
    new_artist(artist)
    return choose_artist(artist)

def get_albums(artist):
    albums = [{'name': alb.name, 'on': str(artist.Album_dict[alb])} for alb in artist.Album_dict]
    return albums

def new_artist(artist):
    artists.extend(user_data.return_artists([artist]))
    artist_data.append({'name': artists[-1].name, 'val': str(len(artists) - 1)})

def new_song(game):
    game_songs = game.new_battle()
    songs = [{'name': game_songs[x].name, 'val': str(x)} for x in range(len(game_songs))]
    return songs, game_songs

def top_ten(game):
    game_ten = game.showSongStats()
    tops = [{'name': game_ten[x].name} for x in range(len(game_ten))]
    return tops

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)