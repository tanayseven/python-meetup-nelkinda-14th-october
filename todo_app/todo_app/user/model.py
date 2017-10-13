from sqlalchemy import ForeignKey

from todo_app.extensions import db


class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64))


class AdminModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey(UserModel.id))
    user = db.relationship(UserModel)
    email = db.Column(db.String(128), unique=True)
