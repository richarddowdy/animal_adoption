from flask_sqlalchemy import SQLAlchemy  

db = SQLAlchemy()

def connect_db(app):

    db.app = app
    db.init_app(app)

class Pet(db.Model):
    """Pets"""

    __tablename__ = "pets"

    id = db.Column(db.Integer,
                   primary_key=True,
                   autoincrement=True)

    name = db.Column(db.String(25),
                     nullable=False)

    species = db.Column(db.String(25),
                        nullable=False)

    photo_url = db.Column(db.Text,
                          default="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRqcpQuKG8uBr-KMokrLyk-5VWzFGBzx2bUUT2ZGhCgs2xdwxAfSg&s",
                          nullable=True)
    
    age = db.Column(db.Integer,
                    nullable=False)

    notes = db.Column(db.Text,
                      nullable=True)
    
    available = db.Column(db.Boolean,
                          nullable=False,
                          default=True)

