from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Student(db.Model, UserMixin):
    student_id = db.Column(db.Integer, primary_key=True)
    matric = db.Column(db.String(10), unique=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    student_lesson = db.Column(db.Integer, db.ForeignKey('lessons.lesson_id'))


class Lessons(db.Model):
    lesson_id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(150))
    participants = db.relationship('Student')


class Tutors(db.Model):
    tutor_id = db.Column(db.Integer, primary_key=True)
    lessons = db.Column(db.String(100))
    password = db.Column(db.String(150))
    name = db.Column(db.String(100))
    matric = db.Column(db.Integer)
