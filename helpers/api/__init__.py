from flask_restful import Api

from resources.OcupacaoResources import InsertOcupacoes, UpSolr, BuscadorOcupacoes

api = Api()

api.add_resource(InsertOcupacoes, "/insert_dataset")
api.add_resource(UpSolr, "/up_solr")
api.add_resource(BuscadorOcupacoes, "/ocupacoes/buscar")