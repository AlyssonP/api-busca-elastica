from flask_restful import Api

from resources.OcupacaoResources import OcupacaoResource, InsertOcupacoes, UpSolr, BuscadorOcupacoes
from resources.IndexResources import IndexResource

api = Api()

api.add_resource(IndexResource, "/")

api.add_resource(OcupacaoResource, "/ocupacoes")
api.add_resource(InsertOcupacoes, "/insert_dataset")
api.add_resource(UpSolr, "/up_solr")
api.add_resource(BuscadorOcupacoes, "/ocupacoes/buscar")
