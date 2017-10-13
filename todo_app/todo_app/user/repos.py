from todo_app.extensions import db
from todo_app.user.models import AdminModel, UserModel, ListUserModel


class UserRepo:
    model = UserModel
    db = db

    @classmethod
    def add_new_user(cls, user_name, password):
        new_user = cls.model()
        new_user.user_name = user_name
        new_user.password = password
        cls.db.session.add(new_user)
        cls.db.session.commit()
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
        cls.db.session.add(new_admin)
        cls.db.session.commit()

    @classmethod
    def fetch_user_for(cls, user_name, password):
        return cls.db.session.query(cls.model).join(UserModel) \
            .filter(UserModel.user_name == user_name).filter(UserModel.password == password).one_or_none()


class ListUserRepo:
    model = ListUserModel
    db = db

    @classmethod
    def load_user_if_exists(cls, auth_token):
        pass
