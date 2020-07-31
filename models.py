"""Models for adopt app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    """Connect this database to provided Flask app.

    You should call this in your Flask app.
    """

    db.app = app
    db.init_app(app)

class Pet(db.Model):
    __tablename__ = 'pets'

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.String(20), nullable=False, unique=True)
    species = db.Column(db.String(20), nullable=False)
    photo_url = db.Column(db.String(250), default='')
    age = db.Column(db.String(20), nullable=False, unique=True)
    notes = db.Column(db.String, nullable=True)
    available = db.Column(db.Boolean, nullable=False, default=True)

    def __repr__(self):
        """Show info about User."""

        p = self
        return f"<Pet {p.id} {p.name} {p.species} {p.photo_url} {p.age} {p.notes} {p.available}>"
