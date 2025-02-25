from flask_restful import Resource
import socket

class IndexResource(Resource):
    def get(self):
        hostname = socket.gethostname()
        return {"version":"1.0", "hostname": hostname}, 200