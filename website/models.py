from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    matric = db.Column(db.String(10), unique=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    tutor = db.Column(db.String(3))
    notes = db.relationship('Note')

class Lessons(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(150))
    participants = db.relationship('User')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
