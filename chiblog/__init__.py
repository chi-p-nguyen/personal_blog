from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from chiblog.config import Config
import click
from flask.cli import with_appcontext
from werkzeug.security import generate_password_hash

db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    login_manager.init_app(app)

    from chiblog.Blog.blog_routes import blog
    from chiblog.User.user_routes import user
    from chiblog.Main.main_routes import main
    from chiblog.Project.project_routes import project

    app.register_blueprint(blog)
    app.register_blueprint(user)
    app.register_blueprint(main)
    app.register_blueprint(project)

    from chiblog.User.user_model import User

    @click.command(name='create_admin')   
    @with_appcontext
    def create_admin():
        admin=User(email="test@gmail.com",password="password")
        admin.password = generate_password_hash(admin.password,'sha256',salt_length=12)
        db.session.add(admin)
        db.session.commit()

    app.cli.add_command(create_admin)

    return app