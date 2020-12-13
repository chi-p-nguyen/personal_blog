from flask import render_template, Blueprint, request, redirect, url_for, flash
from flask_login import login_required
from chiblog import db
from chiblog.Project.project_model import Project

main = Blueprint("main", __name__)

@main.route('/')
@main.route('/home', methods=['GET'])
def home():
    return render_template('home.html')

@main.route('/about')
def about():
    about = Project.query.filter_by(name="About").first()
    if not about:
        about = Project(name="About", description='Hello world', link='my resume')
        db.session.add(about)
        db.session.commit()
    return render_template('about.html', title='About', about=about)

@main.route('/contact')
def contact():
    return render_template('contact.html', title='Contact')

@main.route('/about/edit', methods=['GET', 'POST'])
@login_required
def edit_about():
    about = Project.query.filter_by(name="About").first()
    if request.method == 'POST':
        if about:
            about.description = request.form["abouty"]
            about.link = request.form["resume"]
        else:
            about = Project(name="About", description=request.form["abouty"], link=request.form["resume"])
            db.session.add(about)
        db.session.commit()
        flash('Your about page has been updated', 'dark')
        return redirect(url_for('main.about'))
    return render_template('edit_about.html', title='Edit about', legend='Edit about', about=about)
