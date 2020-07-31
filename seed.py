from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

# Add users
cat = Pet(name='xyz', species='cat',age=2)
dog = Pet(name='abc', species='dag', age=5)
rabbit = Pet(name='def', species='rabbit', age=4)

db.session.add(cat)
db.session.add(dog)
db.session.add(rabbit)

db.session.commit()