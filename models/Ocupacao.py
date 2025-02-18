from flask_restful import fields

from helpers.database import db

ocupacao_fields = {
    "id": fields.Integer,
    "titulo": fields.String
}

pagination_ocupacao_fields = {
    "total": fields.Integer,
    "pages": fields.Integer,
    "current_page": fields.Integer,
    "per_page": fields.Integer,
    "has_next": fields.Boolean,
    "has_prev": fields.Boolean,
    "ocupacoes": fields.List(fields.Nested(ocupacao_fields))
}

class Ocupacao(db.Model):
    __tablename__ = "ocupacoes_tb"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(255), nullable=False)