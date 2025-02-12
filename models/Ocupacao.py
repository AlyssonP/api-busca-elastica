from helpers.database import db

class Ocupacao(db.Model):
    __tablename__ = "ocupacoes_tb"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(255), nullable=False)