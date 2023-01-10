from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class SubmitAnagram(FlaskForm):
    anagram = StringField('Anagram', validators=[DataRequired(), Length(min=2, max=10)])
    submit = SubmitField('Submit')

