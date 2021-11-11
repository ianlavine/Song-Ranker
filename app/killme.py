from app import app, db
from app.forms import RegistrationForm
from flask import request, render_template, url_for, redirect
import Ranking
from app.forms import newArtistForm, selectArtistForm, LoginForm
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Artist, Album, Song
from werkzeug.urls import url_parse
import user_data

# artists = user_data.return_artists(None)
# db.session.expire_on_commit = False
artist = []

game = None 
game_songs = [None, None]
song_data = []
album_data = [] 
topten = []
topalb = []
user = None

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():

    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, rounds=0)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route("/ranks", methods=['GET', 'POST'])
@login_required
def ranks():

    user = User.query.filter_by(username=current_user.username).first_or_404()
    artistform = update_artist_form(user)

    topten = [{'name': x.name, 'score': int(x.score)} for x in song_data]
    topalb = [{'name': x.name, 'score': int(x.score)} for x in album_data]

    if artistform.select_artist.data != None:

        update_data(artistform)

        song_data.sort()
        topten = [{'name': x.name, 'score': int(x.score)} for x in song_data]

        for alb in album_data:
            alb.score = sum([s.score for s in alb.songs.all()]) / len(alb.songs.all())
            db.session.add(alb)
        db.session.commit()

        album_data.sort()
        topalb = [{'name': x.name, 'score': int(x.score)} for x in album_data]

    return render_template('ranks.html', artistform=artistform, topten=topten, topalb=topalb)


@app.route("/index", methods=['GET', 'POST'])
@login_required
def index():


    global game_songs, album_data, song_data, artist, topten

    user = User.query.filter_by(username=current_user.username).first_or_404()
    artistform = update_artist_form(user)

    newform = newArtistForm()
    if newform.validate_on_submit():

        newArtist = user_data.return_artists([newform.new_artist.data])[0]

        art = Artist(name=newArtist.name, owner=user, rounds=0)
        db.session.add(art)
        for alb in newArtist.Albums:
            album = Album(name=alb.name, in_use=True, owner=art, score=0)
            db.session.add(album)
            for so in alb.Songs:
                song = Song(name=so.name, score=1000, owner=album)
                db.session.add(song)
        db.session.commit()
        artistform = update_artist_form(user)
        
    if artistform.select_artist.data != None:
        update_data(artistform)
        game_songs = Ranking.new_battle(song_data)


    song1 = request.args.get("song1", "")
    song2 = request.args.get("song2", "")
    if song1 or song2:
        if song1:
            Ranking.compare(game_songs[0], game_songs[1])
        if song2:
            Ranking.compare(game_songs[1], game_songs[0])
        
        # user.rounds += 1
        # artist.rounds += 1

        # db.session.add(user)
        # db.session.add(artist)
        db.session.add(game_songs[0])
        db.session.add(game_songs[1])
        db.session.commit()

        song_data.sort()
        topten = [{'name': x.name, 'score': int(x.score)} for x in song_data]

        game_songs = Ranking.new_battle(song_data)

    return render_template('index.html', album_data=album_data, songa=game_songs[0], songo=game_songs[1], newform=newform, artistform=artistform, topten=topten)


def update_data(form):

    global artist, album_data, song_data

    artist = Artist.query.filter_by(id=form.select_artist.data).first_or_404()
    album_data = [alb for alb in artist.albums.all()]
    song_data = [song for alb in album_data for song in alb.songs.all()]

def update_artist_form(user):
    form = selectArtistForm()
    form.select_artist.choices = [(x.id, x.name) for x in user.artists.all()]
    return form
