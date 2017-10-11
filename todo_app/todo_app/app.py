from flask import Flask
from flask_admin import Admin


app = Flask(__name__)
admin = Admin(app, name='todo_app', template_mode='bootstrap3')
