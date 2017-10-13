from todo_app.user.model import AdminModel, UserModel
from todo_app.extensions import db


class UserRepo:
    model = UserModel
    db = db

    @classmethod
    def add_new_user(cls, user_name, password):
        new_user = cls.model()
        new_user.user_name = user_name
        new_user.password = password
        cls.db.add(new_user)
        cls.db.commit()
        return new_user


class AdminRepo:
    model = AdminModel
    db = db

    @classmethod
    def add_new_admin(cls, user_name, password, email):
        new_user = UserRepo.add_new_user(user_name, password)
        new_admin = cls.model()
        new_admin.user = new_user
        new_admin.email = email
        cls.db.add(new_admin)
        cls.db.commit()
