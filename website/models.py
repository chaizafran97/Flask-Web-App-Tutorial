from sqlalchemy.sql.expression import column
from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    matric = db.Column(db.String(10), unique=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    kulliyah = db.Column(db.String(5))
    program = db.Column(db.String(5))
    email = db.Column(db.String(100))
    roles = db.Column(db.String(10))

class Lessons(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subCode = db.Column(db.String(15))
    subName = db.Column(db.String(150))
    lesson_date = db.Column(db.String(25))
    lesson_time = db.Column(db.String(25))

class Lesson_User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userMatric = db.Column(db.String(10))
    lessonCode = db.Column(db.String(15))
    lessonName = db.Column(db.String(150))
    lessonDate = db.Column(db.String(25))
    lessonTime = db.Column(db.String(25))