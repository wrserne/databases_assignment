"""Forms for playlist app."""

from wtforms import SelectField
from flask_wtf import FlaskForm

from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Length
from flask_wtf import FlaskForm


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    name = StringField('Name', validators=[DataRequired(), Length(max=50)])
    description = TextAreaField('Description', validators=[DataRequired(), Length(max=250)])


class SongForm(FlaskForm):
    """Form for adding songs."""

    title = StringField('Title', validators=[DataRequired(), Length(max=100)])
    artist = StringField('Artist', validators=[DataRequired(), Length(max=100)])


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)
