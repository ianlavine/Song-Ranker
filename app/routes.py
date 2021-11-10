from app import app
from flask import request, render_template, url_for, redirect
import Ranking
from app.forms import newArtistForm, selectArtistForm, LoginForm
import user_data

artists = user_data.return_artists(None)

game = None 
game_songs = [None, None]
song_data = []
album_data = [] 
topten = []

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)

@app.route("/index", methods=['GET', 'POST'])
def index():

    global game, game_songs, album_data, topten, song_data

    newform = newArtistForm()
    if newform.validate_on_submit():
        artists.extend(user_data.return_artists([newform.new_artist.data]))

    artistform = selectArtistForm()
    artistform.select_artist.choices = [(str(x), artists[x].name) for x in range(len(artists))]
    if artistform.select_artist.data != None:
        artist = artists[int(artistform.select_artist.data)]

        album_data = [alb for alb in artist.Album_dict]

        song_data = [song for alb in album_data for song in alb.Songs]

        game_songs = Ranking.new_battle(song_data)

    song1 = request.args.get("song1", "")
    song2 = request.args.get("song2", "")
    if song1 or song2:
        if song1:
            Ranking.compare(game_songs[0], game_songs[1])
        if song2:
            Ranking.compare(game_songs[1], game_songs[0])
        game_songs = Ranking.new_battle(song_data)
        topten = [{'name': x.name, 'score': int(x.score)} for x in Ranking.showSongStats(song_data)]

    return render_template('index.html', album_data=album_data, songa=game_songs[0], songo=game_songs[1], topten=topten, newform=newform, artistform=artistform)