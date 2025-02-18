from flask_restful import Resource

class IndexResource(Resource):
    def get(self):
        return {"version":"1.0"}, 200