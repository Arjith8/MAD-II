from flask_restful import reqparse, Resource, marshal, fields
from flask import request
from database.models import UserInfo, Songs
from database.models import db

song_type={
    "song_id":fields.Integer,
    "song_name":fields.String,
    "genre":fields.String,
    "release_date":fields.String,
    "playback_count":fields.Integer,
    "rating":fields.Float,
    "duration":fields.Float,
}

response_type = {
    "id" : fields.Integer,
    "name" : fields.String,
    "songs" : fields.List(fields.Nested(song_type))
}

class fetchCreator(Resource):
    def __init__(self):
        self.parser=reqparse.RequestParser()
        self.parser.add_argument('creator_id',type=int, location='args')
        self.parser.add_argument('creator_count',type=int,location='args')

    def get(self):
        args = self.parser.parse_args()
        if '/creators' in request.url:
            creator_count = args['creator_count']
            if not creator_count:
                creator_count = 5
            data = Songs.query.group_by(Songs.singer_id).order_by(db.func.sum(Songs.playback_count).desc()).limit(creator_count)
            singer_data = []
            for i in data:
                singer_id = i.singer_id
                singer_nmae = i.creator_data.username
                singer_data.append({
                    'id':singer_id,
                    'name':singer_nmae
                })
            return singer_data
        
        if not args['creator_id']:
            return {
                "msg":"Creator ID was not provided"
            },400
        try:
            data = UserInfo.query.filter(UserInfo.user_id==args['creator_id'],UserInfo.account_type=='creator').one()
            songs = data.songs
            print('hi')

            if not songs:
                return {
                    "msg" : "The creator hasn't uploaded anything"
                }
            print('hi')
            
            return marshal({
                "id" : data.user_id,
                "name" : data.username,
                "songs" : [{
                    "song_id":i.song_id,
                    "song_name":i.song_name,
                    "genre":i.genre,
                    "release_date":i.release_date,
                    "playback_count":i.playback_count,
                    "rating":format((i.rating_sum/i.count),'.2f') if i.count!=0 else None,
                    "duration":i.duration,
                }for i in songs]
            },response_type)

        except:
            return {
                "msg":"Invalid Creator ID"
            }


        
        

