from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from datetime import datetime


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    matric = db.Column(db.String(10), unique=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    kulliyah = db.Column(db.String(5))
    program = db.Column(db.String(5))
    email = db.Column(db.String(100))
    roles = db.Column(db.String(10))
    lesson = db.Column(db.Integer, db.ForeignKey('lessons.id'))

class Lessons(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subCode = db.Column(db.String(15))
    subName = db.Column(db.String(150))
    lesson_date = db.Column(db.String(25))
    lesson_time = db.Column(db.String(25))
    participants = db.relationship('User')

