from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, Lessons, Lesson_User
from werkzeug.security import generate_password_hash, check_password_hash
from . import db
from flask_login import login_user, login_required, logout_user, current_user
from sqlalchemy import or_

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        matric = request.form.get('matric')
        password = request.form.get('password')
        user = User.query.filter_by(matric=matric).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password, try again.', category='error')
        else:
            flash('Matric number is not registered', category='error')

    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route("/search", methods=['GET', 'POST'])
@login_required
def search():
    courseCode = ''
    if request.method == "POST":
        if request.form.get('search') == 'search':
            courseCode = request.form.get('courseCode')
    return render_template("search.html", user=current_user, query = Lessons.query.filter((Lessons.tutorName.contains(courseCode)) | (Lessons.subCode==courseCode)))

@auth.route("/enrolled", methods=['GET', 'POST'])
@login_required
def enrolled():
    if request.form.get("enrolled"):
        lessonID = request.form.get('enrolled')
        temp = Lessons.query.get(lessonID)
        tempAdd = Lesson_User(userMatric=current_user.matric,lessonCode=temp.subCode,lessonName=temp.subName,lessonDate=temp.lesson_date,lessonTutor=temp.tutorName,lessonNotes=temp.notes)
        db.session.add(tempAdd)
        db.session.commit()
    return render_template("enrolled.html", user=current_user, query=Lesson_User.query.filter_by(userMatric=current_user.matric))

@auth.route("/deleted", methods=['GET', 'POST'])
@login_required
def deleted():
    if request.form.get("deleted"):
        lessonID = request.form.get('deleted')
        Lesson_User.query.filter_by(id=lessonID).delete()
        db.session.commit()
    return render_template("deleted.html", user=current_user)

@auth.route('/classes', methods=['GET', 'POST'])
@login_required
def classes():
    if request.form.get("enrolled"):
        lessonID = request.form.get('enrolled')
        temp = Lessons.query.get(lessonID)
        tempAdd = Lesson_User(userMatric=current_user.matric,lessonCode=temp.subCode,lessonName=temp.subName,lessonDate=temp.lesson_date)
        db.session.add(tempAdd)
        db.session.commit()
    return render_template("classes.html", user=current_user, query=Lessons.query.all())

@auth.route('/addClass', methods=['GET', 'POST'])
@login_required
def addClass():
    if request.method == 'POST':
        subName = request.form.get('subName')
        subCode = request.form.get('subCode')
        lesson_date = request.form.get('lesson_date')
        tutorName = request.form.get('tutorName')
        notes = request.form.get('notes')

        new_sub = Lessons.query.filter_by(subName=subName).first()
        if len(subCode) < 3:
            flash('Subject code is too short!', category='error')
        else:
            new_sub = Lessons(subCode=subCode, subName=subName, lesson_date=lesson_date, tutorName=tutorName, notes=notes)
        db.session.add(new_sub)
        db.session.commit()
        flash('Lesson added!', category='success')
    return render_template("addClass.html", user=current_user)

@auth.route('/SignUpOptions')
def signUpOptions():

    return render_template("signUpOptions.html", user=current_user)

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        matric = request.form.get('matric')
        name = request.form.get('name')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')
        kulliyah = request.form.get('kulliyah')
        program = request.form.get('program')
        email = request.form.get('email')

        user = User.query.filter_by(matric=matric).first()
        if user:
            flash('Matric number has been registered', category='error')
        elif name is None:
            flash('Name must be greater than 1 character.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match.', category='error')
        elif len(password1) < 7:
            flash('Password must be at least 7 characters.', category='error')
        else:
            if len(matric) == 7:
                new_user = User(matric=matric, name=name, password=generate_password_hash(
                password1, method='sha256'), kulliyah=kulliyah, program=program, email=email, roles="student")
            else:
                new_user = User(matric=matric, name=name, password=generate_password_hash(
                password1, method='sha256'), kulliyah=kulliyah, program=program, email=email, roles="tutor")
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user, remember=True)
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))    

    return render_template("sign_up.html", user=current_user)
