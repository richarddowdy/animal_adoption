from models import Pet, db
from app import app

db.drop_all()
db.create_all()

sparky = Pet(name="Sparky", species="dog", age=20, notes="awesome")

fido = Pet(name="Fido", species="cat", photo_url="https://upload.wikimedia.org/wikipedia/commons/thumb/7/77/Avatar_cat.png/120px-Avatar_cat.png", age=50, available=False)

# db.session.add_all([sparky, fido])
db.session.add(sparky)
db.session.add(fido)
db.session.commit()

