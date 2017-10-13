from todo_app.extensions import db


class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(64))
