from flask import Flask

from helpers.database import db
from helpers.cors import cors
from helpers.api import api
import models

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:123456@127.0.0.0:5431/cbo_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app=app)
with app.app_context():
    db.create_all()

cors.init_app(app=app)
api.init_app(app=app)

if __name__ == "__main__":
    app.run()