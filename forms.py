import flask_wtf import FlaskForm
import wtforms import StringField


class AddPetForm(FlaskForm):
    """Form for adding pets."""
    name = StringField("Pet Name: ")
    species = StringField("Pet Species: ")
    photo_url = StringField("Pet Photo URL: ")
    age = StringField("Pet Age: ")
    notes = TextAreaField("Additional Notes: ")