from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# Add users
cat = Pet(name='xyz', species='cat',age='baby')
dog = Pet(name='abc', species='dog', age='adult')
rabbit = Pet(name='def', species='porcupine', age='adult')

db.session.add(cat)
db.session.add(dog)
db.session.add(rabbit)

db.session.commit()