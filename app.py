"""Flask app for adopt app."""

from flask import Flask, render_template,redirect

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet

from forms import AddPetForm, EditPetForm

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
        photo_url = add_pet_form.photo_url.data 
        age = add_pet_form.age.data
        notes = add_pet_form.age.data or None

        new_pet = Pet(name = name, species = species, photo_url = photo_url, age = age, notes = notes)
        db.session.add(new_pet)
        db.session.commit()
        return redirect("/")
    else:
        return render_template('add_pet.html', form = add_pet_form)

@app.route('/<int:pet_id_number>', methods = ['GET', 'POST'])
def edit_pet(pet_id_number):
    """Shows some information about the pet and an edit pet form; processes form for editting a pet."""
    current_pet = Pet.query.get(pet_id_number)
    edit_pet_form = EditPetForm(obj=current_pet)

    if  edit_pet_form.validate_on_submit():

        current_pet.photo_url = edit_pet_form.photo_url.data
        current_pet.notes = edit_pet_form.notes.data or None
        current_pet.available = edit_pet_form.available.data

        db.session.commit()

        return redirect(f"/{pet_id_number}")
    else:
        return render_template('/edit_pet.html', form = edit_pet_form, pet = current_pet)