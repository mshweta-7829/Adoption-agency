from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, Email, URL


class AddPetForm(FlaskForm):
    """Form for adding pets."""
    name = StringField("Pet Name: ", validators=[InputRequired()])
    species = SelectField('Species',
              choices=[('cat', 'Cat'), ('dog', 'Dog'), ('porcupine', 'Porcupine')])
    age = SelectField('Age',
          choices=[('baby', 'Baby'), ('young', 'Young'), ('adult', 'Adult'), ('senior', 'Senior')])
    photo_url = StringField("Photo URL: ", validators=[Optional(), URL()])
    notes = TextAreaField("Additional Notes: ")

class EditPetForm(FlaskForm):
    """Form for editing pets."""
    photo_url = StringField("Photo URL: ", validators=[Optional(), URL()])
    notes = TextAreaField("Additional Notes: ", validators=[Optional()])
    available = BooleanField("Availability: ") #TODO change if there's anything to validate