from app import db
from app.main import bp
from app.main.forms import newArtistForm, selectArtistForm
from flask import request, render_template
import Ranking
from flask_login import current_user, login_required
from app.models import User, Artist, Album, Song
import user_data

artist = None

game_songs = [None, None]
images = [None, None]
song_data = []
album_data = [] 
album_data_off = []
topten = []
topalb = []
user = None
ordered = []
to_show = None
sort_albs = []
alber = None

@bp.route("/ranks", methods=['GET', 'POST'])
@login_required
def ranks():

    global ordered, to_show, sort_albs, artist, topten, ordered, song_data, album_data, alber

    alber = request.args.get("alber", "")

    newform, artistform = form_checks()

    if alber:
        to_show = sort_albs[int(alber)]
        db.session.add(to_show)
        db.session.commit()
        temp = [x for x in to_show.songs.all()]
        temp.sort()
        ordered = [{'name': x.name, 'score': int(x.score)} for x in temp]
    else:
        to_show = None
        ordered = []

    return render_template('main/ranks.html', artistform=artistform, newform=newform, sort_albs=sort_albs, topten=topten, art=artist, ordered=ordered, to_show=to_show)


@bp.route("/index", methods=['GET', 'POST'])
@login_required
def index():

    global game_songs, album_data, album_data_off, song_data, topten, artist, images

    newform, artistform = form_checks()

    alber = request.args.get("alber", "")
    alber2 = request.args.get("alber2", "")
    to_change = None
    if alber or alber2:
        if alber2:
            to_change = album_data_off[int(alber2)]
        elif len(album_data) > 1:
            to_change = album_data[int(alber)]
    if to_change != None:
        to_change.swap()
        db.session.add_all([artist, to_change])
        db.session.commit()
        update_albums()
        game_songs = Ranking.new_battle(song_data)

    sonny = request.args.get("songer", "")
    if sonny and artist:
        if int(sonny) == 0:
            Ranking.compare(game_songs[0], game_songs[1])
        if int(sonny) == 1:
            Ranking.compare(game_songs[1], game_songs[0])
        
        user.rounds += 1
        artist.rounds += 1

        local_user = db.session.merge(user)
        local_artist = db.session.merge(artist)
        local_song0 = db.session.merge(game_songs[0])
        local_song1 = db.session.merge(game_songs[1])
        db.session.add_all([local_user, local_artist, local_song0, local_song1])
        db.session.commit()

        song_data.sort()
        topten = [{'name': x.name, 'score': int(x.score)} for x in song_data]

        game_songs = Ranking.new_battle(song_data)

    if game_songs[0] != None and artist != None:
        for s in range(len(game_songs)):
            local_song = db.session.merge(game_songs[s])
            local_owner = db.session.merge(local_song.owner)
            images[s] = local_owner.cover
            db.session.add_all([local_song, local_owner])
            db.session.commit()

    return render_template('main/index.html', album_data=album_data, album_data_off=album_data_off, game_songs=game_songs, images=images, newform=newform, artistform=artistform, topten=topten, art=artist)


def form_checks():

    global user, artist, game_songs, topten, sort_albs, alber

    user = User.query.filter_by(username=current_user.username).first_or_404()
    artistform = update_artist_form(user)

    newform = newArtistForm()
    if newform.validate_on_submit():

        newArtist = user_data.return_artists([newform.new_artist.data])[0]

        name = newArtist.name
        if name not in [x.name for x in user.artists.all()]:

            art = Artist(name=newArtist.name, owner=user, rounds=0)
            db.session.add(art)
            for alb in newArtist.Albums:
                album = Album(name=alb.name, in_use=True, owner=art, score=0, cover=alb.Cover)
                db.session.add(album)
                for so in alb.Songs:
                    song = Song(name=so.name, score=1000, owner=album)
                    db.session.add(song)
            db.session.commit()
            artistform = update_artist_form(user)
        
    if artistform.select_artist.data != None:

        if artistform.submit.data:
            artist = Artist.query.filter_by(id=artistform.select_artist.data).first_or_404()
            update_albums()
            game_songs = Ranking.new_battle(song_data)

            temp_sort = sorted(song_data)
            topten = [{'name': x.name, 'score': int(x.score)} for x in temp_sort]

            for alb in album_data:
                alb.score = sum([s.score for s in alb.songs.all()]) / len(alb.songs.all())
                db.session.add(alb)
                db.session.add(artist)
                db.session.add_all([alb, artist])
            db.session.commit()

            sort_albs = sorted(album_data)

            alber = None

        elif artistform.remove.data:

            temp_artist = Artist.query.filter_by(id=artistform.select_artist.data).first_or_404()

            artist = None

            for alb in temp_artist.albums.all():
                for s in alb.songs.all():
                    db.session.delete(s)
                db.session.delete(alb)
            db.session.delete(temp_artist)
            db.session.commit()

            artistform = update_artist_form(user)

    return (newform, artistform)
    

def update_albums():

    global artist, album_data, album_data_off, song_data, game_songs

    if artist is None:
        album_data = []
        album_data_off = []
        song_data = []
        game_songs = [None, None]

    else:
        album_data = [alb for alb in artist.albums.all() if alb.in_use]
        album_data_off = [alb for alb in artist.albums.all() if not alb.in_use]
        song_data = [song for alb in album_data for song in alb.songs.all()]


def update_artist_form(user):
    form = selectArtistForm()
    form.select_artist.choices = [(x.id, x.name) for x in user.artists.all()]
    form.length = len(form.select_artist.choices)
    return form

