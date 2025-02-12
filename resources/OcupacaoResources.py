from flask_restful import Resource
import csv

from helpers.database import db
from models.Ocupacao import Ocupacao

def dataset_ocupacao_csv(path):
    data = []
    with open(path, encoding="ISO-8859-1") as csv_file:
        read = csv.reader(csv_file)
        next(read, None)
        print(type(read))
        for row in read:
            spliter = row[0].split(";")
            # data.append({"id":int(spliter[0]), "titulo":str(spliter[1])})
            data.append(Ocupacao(
                id=int(spliter[0]),
                titulo=str(spliter[1])
                ))
    return data

class InsertOcupacoes(Resource):
    def post(self):
        if(len(Ocupacao.query.all())>0):
            return {"message":"Os dados já foram inseridos"}, 409
        
        ocupacoes = dataset_ocupacao_csv("/home/alyssonp/gcsi20242/app-busca-elastica/CBO2002 - Ocupacao.csv")
        try:
            db.session.add_all(ocupacoes)
            db.session.commit()
            return {"message":"Dados inseridos com sucesso!"}, 200
        except Exception as e:
            db.session.rollback()
            return {"message": "Ocorreu um erro ao tentar inserir os dados do csv", "error": str(e)}, 500
