from flask_restful import Api

from resources.OcupacaoResources import InsertOcupacoes

api = Api()

api.add_resource(InsertOcupacoes, "/insert_dataset")