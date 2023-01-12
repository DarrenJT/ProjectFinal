from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.secret_key = "Secret Key"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Oscarthur19#@127.0.0.1:3306/crud'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db = SQLAlchemy(app)

from application import routes