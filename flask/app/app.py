from flask import Flask
from config import Configuration
from flask_sqlalchemy import SQLAlchemy     # ORM (object relation model) system
from flask_migrate import Migrate
from flask_script import Manager

app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)
manager.add_command('db', Migrate)