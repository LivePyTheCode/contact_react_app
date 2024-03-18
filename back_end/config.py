from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
import os
from dotenv import load_dotenv

FLASK_KEY = os.getenv('FLASK_KEY')
DB = os.getenv('DB')

app = Flask(__name__, static_folder='front_end/dist', static_url_path='')
CORS(app)
app.config['SECRET_KEY'] = FLASK_KEY

app.config["SQLALCHEMY_DATABASE_URI"] = DB
app.config["SQLALCHEMY_TRACK_MODICATIONS"] = False

db = SQLAlchemy(app)

 
