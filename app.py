"""Flask app for adopt app."""

from flask import Flask, render_template,redirect

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet

from forms import AddPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)
db.create_all()

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

@app.route("/")
def show_home_page():
    """ renders the home page """

    pet_details = Pet.query.all()
    print (f"LOOKING FOR THIS{pet_details}")
    return render_template("index.html", pet_details=pet_details)

@app.route('/add', methods=['GET', 'POST'])
def add_pet():
    """Shows a form for adding pet (GET); processes form for adding a pet (POST)."""
    
    add_pet_form = AddPetForm()

    if add_pet_form.validate_on_submit():
        name = add_pet_form.name.data
        species = add_pet_form.species.data
        photo_url = add_pet_form.photo_url.data #TODO check if error
        age = add_pet_form.age.data
        notes = add_pet_form.age.data or None

        #DEBUG if needed add print statement

        new_pet = Pet(name = name, species = species, photo_url = photo_url, age = age, notes = notes)
        db.session.add(new_pet)
        db.session.commit()
        return redirect("/")
    else:
        return render_template('add_pet.html', form = add_pet_form)