from app import db, login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    artists = db.relationship('Artist', backref='owner', lazy='dynamic')
    rounds = db.Column(db.Integer())

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    albums = db.relationship('Album', backref='owner', lazy='dynamic')
    rounds = db.Column(db.Integer())

    def __repr__(self):
        return '<Post {}>'.format(self.name)

class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    in_use = db.Column(db.Boolean)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'))
    songs = db.relationship('Song', backref='owner', lazy='dynamic')
    score = db.Column(db.Integer())

    def __repr__(self):
        return '<Post {}>'.format(self.name)

    def __lt__(self, other):
        return self.score > other.score

class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    score = db.Column(db.Integer)
    album_id = db.Column(db.Integer, db.ForeignKey('album.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.name)

    def __lt__(self, other):
        return self.score > other.score

@login.user_loader
def load_user(id):
    return User.query.get(int(id))