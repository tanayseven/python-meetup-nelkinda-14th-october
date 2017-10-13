import os

from flask_migrate import MigrateCommand
from flask_script import Manager

from todo_app.admin.views import register_admin
from todo_app.extensions import app
from todo_app.list.models import ItemModel
from todo_app.user.models import ListUserModel, AdminModel

register_admin(app)
manager = Manager(app)

AdminModel()
ListUserModel()
ItemModel()

print("*** CURRENT ENVIRONMENT: " + os.environ['TODO_APP'] + " ***")


@manager.command
def serve(host='0.0.0.0', port=5000, debug=False):
    app.run(host, port, debug=debug)


@manager.command
def test():
    pass


manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
