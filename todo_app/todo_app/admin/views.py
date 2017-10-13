from flask_admin import Admin, expose, BaseView


class LoginView(BaseView):
    @expose('/', methods=('GET', 'POST',))
    def index(self):
        return 'tototo'


def register_admin(app):
    admin = Admin(name='Dashboard', base_template='login.html')
    admin.add_view(LoginView(name="Login", endpoint='login/'))
    admin.init_app(app)
