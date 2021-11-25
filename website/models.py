from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Student(db.Model, UserMixin):
    student_id = db.Column(db.Integer, primary_key=True)
    matric = db.Column(db.String(10), unique=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    kulliyah = db.Column(db.String(5))
    program = db.Column(db.String(5))
    email = db.Column(db.String(100))
    student_lesson = db.Column(db.Integer, db.ForeignKey('lessons.lesson_id'))


class Lessons(db.Model):
    lesson_id = db.Column(db.Integer, primary_key=True)
    subject_name = db.Column(db.String(150))
    subject_code = db.Column(db.String(15))
    participants = db.relationship('Student')
    start_time = db.Column(db.DateTime)
    end_time = db.Column(db.DateTime)


class Tutors(db.Model):
    tutor_id = db.Column(db.Integer, primary_key=True)
    matric = db.Column(db.Integer)
    password = db.Column(db.String(150))
    name = db.Column(db.String(100))
    kulliyah = db.Column(db.String(5))
    email = db.Column(db.String(100))
    lessons = db.Column(db.String(100))
