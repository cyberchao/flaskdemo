from flask import Flask
from .settings import config
import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config_name=None):
    app = Flask(__name__)
    app.config['UPLOAD_PATH'] = os.path.join(app.root_path, 'uploads')
    app.config.from_object(config['development'])
    from demo.app1.auth import auth_bp
    app.register_blueprint(auth_bp, url_prefix='/auth')
    db.init_app(app)
    return app
