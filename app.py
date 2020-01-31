from flask import Flask, render_template, redirect, flash
from models import db, connect_db, Pet
from forms import AddPetForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "oh-so-secret"
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///PetsDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

@app.route("/")
def root():

    pets = Pet.query.all()
    print(pets)

    return render_template("index.html", pets=pets)

@app.route('/add', methods=["GET", "POST"])
def get_add_form():
    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data
        print("***************Before FLASH")
        flash(f"Added {name} to Adoption List")
        print("***************AFTER FLASH")
        return redirect('/add')
    
    else:
        return render_template('add_pet_form.html', form=form)
