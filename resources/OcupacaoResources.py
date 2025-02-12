from flask_restful import Resource
from flask import request
import csv
import json
import requests

from helpers.database import db
from models.Ocupacao import Ocupacao
from helpers.config import URL_SOLR

def dataset_ocupacao_csv(path):
    data = []
    with open(path, encoding="ISO-8859-1") as csv_file:
        read = csv.reader(csv_file)
        next(read, None)
        print(type(read))
        for row in read:
            spliter = row[0].split(";")
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
        
class UpSolr(Resource):
    def post(self):
        if(len(Ocupacao.query.all())<0):
            return {"message":"Não há dados a ser levantados"}, 409

        ocupacoes = []
        for ocupacao  in Ocupacao.query.all():
            ocupacoes.append({"id":ocupacao.id, "titulo":ocupacao.titulo, "full": f"{ocupacao.id} {ocupacao.titulo}"})

        SOLR_URL = f"{URL_SOLR}/update?commit=true"

        headers = {"Content-Type": "application/json"}
        response = requests.post(SOLR_URL, data=json.dumps(ocupacoes), headers=headers)

        if response.status_code == 200:
            return {"message":"Dados indexados com sucesso!"}, 200
        else:
            return {"message":f"Erro ao indexar: {response.text}"}, 500

class BuscadorOcupacoes(Resource):
    def get(self):
        termo = request.args.get("q", "*:*")  # Pega o termo da query string
        params = {
            "q": termo+"~",
            "wt": "json"
        }

        SOLR_QUERY_URL = f"{URL_SOLR}/select"

        response = requests.get(SOLR_QUERY_URL, params=params)

        if response.status_code == 200:
            return response.json(), 200
        else:
            return {"erro": "Falha na busca"}, 500

