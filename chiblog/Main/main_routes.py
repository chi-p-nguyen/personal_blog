from flask import render_template, Blueprint
from chiblog import db

main = Blueprint("main", __name__)

@main.route('/')
@main.route('/home', methods=['GET'])
def home():
    return render_template('home.html')

@main.route('/about')
def about():
    return render_template('about.html', title='About')

@main.route('/projects', methods=['GET'])
def projects():
    return render_template('projects.html')