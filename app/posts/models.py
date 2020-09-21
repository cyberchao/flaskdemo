from demo import db
from demo.app.user.models import User
from datetime import datetime

class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(300))
    date = db.Column(db.DateTime(),default=datetime.now())
    comments = db.relationship('Comment', backref='content', lazy='dynamic')
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(300))
    date = db.Column(db.DateTime(),default=datetime.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    content_id = db.Column(db.Integer, db.ForeignKey('content.id'))
    def to_json(self):
        dict = self.__dict__
        if "_sa_instance_state" in dict:
            del dict["_sa_instance_state"]
        return dict