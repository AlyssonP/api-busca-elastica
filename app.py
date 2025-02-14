from flask import Flask
from dotenv import load_dotenv
import os

from helpers.database import db
from helpers.cors import cors
from helpers.api import api
import models

if(os.environ.get("env")==None):
    load_dotenv(".env.development")
else:
    load_dotenv(".env.production")

app = Flask(__name__)

try:
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
except Exception as e:
    print("Erro ao tentar conectar ao banco de dados:",e)

db.init_app(app=app)
with app.app_context():
    db.create_all()

cors.init_app(app=app)
api.init_app(app=app)

if __name__ == "__main__":
    app.run()