from flask import Flask
from dotenv import load_dotenv
import os

from helpers.database import db
from helpers.cors import cors
from helpers.api import api

if(os.environ.get("env")=="production"):
    load_dotenv(".env.production")
elif(os.environ.get("env")=="development"):
    load_dotenv(".env.development")

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app=app)
with app.app_context():
    db.create_all()

cors.init_app(app=app)
api.init_app(app=app)

if __name__ == "__main__":
    app.run()
