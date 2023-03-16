
from utils.db import db


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    lastname = db.Column(db.String(100))
    identification = db.Column(db.String(100))
    email = db.Column(db.String(100))

    def __init__(self, name, lastname, identification, email):
        self.name = name
        self.lastname = lastname
        self.identification = identification
        self.email = email