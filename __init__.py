from flask import Flask
from .settings import config
import os
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

bcrypt = Bcrypt()
db = SQLAlchemy()
login_manager = LoginManager()


def create_app(config_name=None):
    app = Flask(__name__)
    app.config['UPLOAD_PATH'] = os.path.join(app.root_path, 'uploads')
    app.config.from_object(config['development'])
    bcrypt.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    from demo.app.user.auth import auth_bp
    from demo.app.main.routes import main_bp
    from demo.app.posts.routes import content_bp
    app.register_blueprint(main_bp, url_prefix='')
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(content_bp, url_prefix='/content')

    return app
