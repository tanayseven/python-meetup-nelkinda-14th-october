import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from todo_app.config import load_config

app = Flask(__name__, template_folder='templates/', static_url_path='')
load_config(app, os.environ['TODO_APP'])
db = SQLAlchemy(app)
migrate = Migrate(app, db)
