from flask import Flask, render_template, redirect, flash
from models import db, connect_db, Pet

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///PetsDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)

@app.route("/")
def root():

    pets = Pet.query.all()

    return render_template("index.html", pets=pets)
