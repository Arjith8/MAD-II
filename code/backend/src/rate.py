from flask_restful import Resource, reqparse
from database.models import Songs, db
from flask_jwt_extended import jwt_required

class rate(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("song_id", required=True, type = int)
        self.parser.add_argument("rating", required=True, type = int)
    
    @jwt_required()
    def post(self):
        args = self.parser.parse_args()
        data = Songs.query.filter_by(song_id = args['song_id']).first()
        if not data:
            return {
                "msg":"Invalid Song ID",
                "success":False
            }
        if args['rating'] < 1 or args['rating'] > 5:
            return {
                "msg":"Invalid rating",
                "success":False
            }
        data.rating_sum += args['rating']
        data.count += 1
        db.session.commit()
        return {
            "msg":"Rating added successfully",
            "success":True
        }
    