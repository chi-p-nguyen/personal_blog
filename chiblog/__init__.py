from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from chiblog.config import Config

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

    app.register_blueprint(blog)
    app.register_blueprint(user)
    app.register_blueprint(main)

    return app