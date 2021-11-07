from flask import Flask, request, render_template
import user_data
import PythonRanker

app = Flask(__name__)

artists = user_data.return_artists(None)
game = None
game_songs = []
album_data = []
song_data = []
topten = []

@app.route("/")
def index():

    global game, game_songs, album_data, song_data, topten

    choice = request.args.get("chosen_artist", "")
    new_choice = request.args.get("new_artist", "")

    if new_choice:
        artists.extend(user_data.return_artists([new_choice]))

    if choice:
        artist = artists[int(choice)]

        album_data = [alb for alb in artist.Album_dict]

        game = PythonRanker.Play(artist)

        game_songs = game.new_battle()

    song_choice = request.args.get("chosen_song", "")
    if song_choice:
        if song_choice == 0:
            game.compare(game_songs[0], game_songs[1])
        else:
            game.compare(game_songs[1], game_songs[0])
        game_songs = game.new_battle()
        topten = [x for x in game.showSongStats()]

    return render_template('index.html', artist_data=artists, album_data=album_data, song_data=game_songs, topten=topten)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)