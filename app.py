from flask import Flask, render_template, redirect, flash
from models import db, connect_db, Pet
from forms import AddPetForm, EditPetForm
from secrets import API_KEY

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
        name = form.name.data or None
        species = form.species.data or None 
        photo_url = form.photo_url.data or None
        age = form.age.data
        notes = form.notes.data
        print("***************Before FLASH")
        flash(f"Added {name} to Adoption List")
        print("***************AFTER FLASH")

        new_pet = Pet(name=name, species=species, photo_url=photo_url, age=age, notes=notes)

        db.session.add(new_pet)
        db.session.commit()


        return redirect('/')
    
    else:
        return render_template('add_pet_form.html', form=form)

@app.route('/<int:pet_id>', methods=['GET', "POST"])
def edit_pet_form(pet_id):

    form = EditPetForm()
    pet = Pet.query.get_or_404(pet_id)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data or "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRqcpQuKG8uBr-KMokrLyk-5VWzFGBzx2bUUT2ZGhCgs2xdwxAfSg&s"
        pet.notes = form.notes.data or None
        pet.available = form.available.data

        db.session.add(pet)
        db.session.commit()

        return redirect('/')

    else:
        return render_template('edit_pet_form.html', form=form, pet=pet)


