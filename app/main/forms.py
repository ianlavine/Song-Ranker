from flask_wtf import FlaskForm
from wtforms import StringField, RadioField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class newArtistForm(FlaskForm):
    new_artist = StringField('New Artist:', validators=[DataRequired()])
    submit = SubmitField('Submit')

class selectArtistForm(FlaskForm):
    select_artist = RadioField("Choose an Artist")
    length = IntegerField('lala')
    submit = SubmitField('Submit')
    remove = SubmitField('Remove')
