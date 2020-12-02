from flask import render_template, Blueprint
from chiblog import db

project = Blueprint("project", __name__)

@project.route('/projects', methods=['GET'])
def projects():
    return render_template('projects.html')