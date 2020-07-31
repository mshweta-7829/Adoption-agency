from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField
from wtforms.validators import InputRequired, Optional, Email, URL


class AddPetForm(FlaskForm):
    """Form for adding pets."""
    name = StringField("Pet Name: ", validators=[InputRequired()])
    species = SelectField('Species',
              choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')])
    age = SelectField('Age',
          choices=[('baby', 'Baby'), ('young', 'Young'), ('adult', 'Adult'), ('senior', 'Senior')])
    photo_url = StringField("Photo-Url: ", validators=[Optional(), URL()])
    notes = TextAreaField("Additional Notes: ")