from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    artists = db.relationship('Artist', backref='owner', lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.username)


class Artist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    albums = db.relationship('Album', backref='owner', lazy='dynamic')

    def __repr__(self):
        return '<Post {}>'.format(self.name)

class Album(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    in_use = db.Column(db.Boolean)
    artist_id = db.Column(db.Integer, db.ForeignKey('artist.id'))
    songs = db.relationship('Song', backref='owner', lazy='dynamic')

    def __repr__(self):
        return '<Post {}>'.format(self.name)

class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64))
    score = db.Column(db.Integer)
    album_id = db.Column(db.Integer, db.ForeignKey('album.id'))

    def __repr__(self):
        return '<Post {}>'.format(self.name)