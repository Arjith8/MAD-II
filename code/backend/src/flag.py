from flask_restful import Resource, reqparse
from database.models import SongFlags, db
from flask_jwt_extended import jwt_required, get_jwt_identity

class flag(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("song_id", required=True, type = int, location='args')

    @jwt_required()
    def post(self):
        user_data = get_jwt_identity()
        args = self.parser.parse_args()
        try:
            data = SongFlags(song_id = args['song_id'], user_id = user_data['id'])
            db.session.add(data)
            db.session.commit()
            return {
                "msg":"Song flagged successfully",
                "success":True
            }
        except:
            return {
                "msg":"Song already flagged",
                "success":False
            }
