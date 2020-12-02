from flask import render_template, url_for, request, flash, Blueprint, redirect
from chiblog import db
from chiblog.Project.project_model import Project
from flask_login import login_required

project = Blueprint("project", __name__)

@project.route('/projects', methods=['GET'])
def projects():
    projects = Project.query.all()
    return render_template('projects.html', title="Projects",projects=projects)

@project.route('/projects/new', methods=['GET', 'POST'])
@login_required
def new_project():
    if request.method == 'POST':
        project = Project(name=request.form["name"], description=request.form["description"], link=request.form["link"])
        db.session.add(project)
        db.session.commit()
        flash('Your project has been added!', 'dark')
        return redirect(url_for('project.projects'))
    return render_template('add_project.html', title="Add project", legend="Add new project")

@project.route("/projects/<int:project_id>/update", methods=['GET', 'POST'])
@login_required
def update_project(project_id):
    project = Project.query.get_or_404(project_id)
    if request.method == "POST":
        project.name = request.form["name"]
        project.description = request.form["description"]
        project.link = request.form["link"]
        db.session.commit()
        flash('Your post has been updated!', 'success')
        return redirect(url_for('project.projects', project_id=project.id))
    return render_template('add_project.html', title="Update Project", legend='Update Project', project=project)

@project.route("/projects/<int:project_id>/delete", methods=['POST'])
@login_required
def delete_project(project_id):
    project = Project.query.get_or_404(project_id)
    db.session.delete(project)
    db.session.commit()
    flash('Your project has been deleted!', 'dark')
    return redirect(url_for('project.projects'))