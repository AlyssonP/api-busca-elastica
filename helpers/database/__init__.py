from flask_sqlalchemy import SQLAlchemy

try:
    db = SQLAlchemy()
except Exception as e:
    print("Erro ao tentar conectar ao banco de dados", e)