from flask import Flask
from config import Configuration

from flask_sqlalchemy import SQLAlchemy     # ORM (object relation model) system


app = Flask(__name__)
app.config.from_object(Configuration)
db = SQLAlchemy(app)

