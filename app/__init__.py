from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from googleapiclient.discovery import build

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'
youtube = build('youtube', 'v3', developerKey='AIzaSyB_6OvKkXQ_g_XA98UwZ4UZvpDbLb9L96E')


from app import routes, models

