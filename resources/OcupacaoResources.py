from flask_restful import Resource
from flask import request
import csv
import json
import requests
import io

from helpers.database import db
from models.Ocupacao import Ocupacao
from helpers.config.solr import URL_SOLR

def dataset_ocupacao_csv(file):
    data = []
    stream = io.StringIO(file.stream.read().decode("ISO-8859-1"))
    reader = csv.reader(stream)
    next(reader, None)
    for row in reader:
        spliter = row[0].split(";")
        data.append(Ocupacao(
            id=int(spliter[0]),
            titulo=str(spliter[1])
        ))
    return data

class InsertOcupacoes(Resource):
    def post(self):
        if "file" not in request.files:
            return {"message":"Arquivo não enviado em file!"}, 400
        
        if(len(Ocupacao.query.all())>0):
            return {"message":"Os dados já foram inseridos"}, 409
        
        file = request.files["file"]
        if(file.filename == ""):
            return {"message": "Não selecionado"}, 400
        
        try:
            ocupacoes = dataset_ocupacao_csv(file)
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
            ocupacoes.append({"id":ocupacao.id, "titulo":ocupacao.titulo})

        SOLR_URL = f"{URL_SOLR}/update?commit=true"
        print(SOLR_URL)

        headers = {"Content-Type": "application/json"}
        response = requests.post(SOLR_URL, data=json.dumps(ocupacoes), headers=headers)

        if response.status_code == 200:
            return {"message":"Dados indexados com sucesso!"}, 200
        else:
            return {"message":f"Erro ao indexar: {response.text}"}, 500

class BuscadorOcupacoes(Resource):
    def get(self):
        termo = request.args.get("q", "*:*")
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

