from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, RadioField, SelectMultipleField, SubmitField, BooleanField
from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import User

class newArtistForm(FlaskForm):
    new_artist = StringField('New Artist:', validators=[DataRequired()])
    submit = SubmitField('Submit')

class selectArtistForm(FlaskForm):
    select_artist = RadioField("Choose an Artist")
    submit = SubmitField('Submit')

class swapAlbumForm(FlaskForm):
    remove = RadioField("In Rotation")
    include = RadioField("Excluded")
    submit = SubmitField('Update')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')
