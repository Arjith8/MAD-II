from flask_restful import Resource,reqparse
from resources.models import Songs


class IndexData(Resource):
    def __init__(self):
        self.parser=reqparse.RequestParser()
        self.parser.add_argument('token',required=True)
        
    def get(self):
        data=Songs.query.order_by(Songs.playback_count.desc()).all()
        print(data)
