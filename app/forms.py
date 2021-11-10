from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, RadioField, SubmitField, BooleanField
from wtforms.validators import DataRequired

class newArtistForm(FlaskForm):
    new_artist = StringField('New Artist:', validators=[DataRequired()])
    submit = SubmitField('Submit')

class selectArtistForm(FlaskForm):
    select_artist = RadioField("Choose an Artist")
    submit = SubmitField('Submit')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Sign In')

# class song1(FlaskForm):
#     song = 
#     submit = SubmitField('Submit')
