from flask_restful import Resource, fields, marshal_with, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from database.models import Favourites, Songs, db

response_type = {
    "id":fields.Integer,
    "name":fields.String,
    "singer_name":fields.String,
    "genre":fields.String,
    "releaseDate":fields.String,
    "playbackCount":fields.Integer,
    "rating":fields.Float,
    "duration":fields.Float,
    "favorited_on" : fields.String
}

class favourites(Resource):
    def __init__(self) :
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("favourites_count",location = "args", type = int)
        self.parser.add_argument("song_id",location = "args", type = int)

    @jwt_required()
    @marshal_with(response_type)
    def get(self):
        args = self.parser.parse_args()
        user_data = get_jwt_identity()
        favourites_count = args['favourites_count']
        if not favourites_count:
            favourites_count = 5
        data = Favourites.query.filter_by(user_id = user_data['data']['user_id']).order_by(Favourites.favorited_on.desc()).limit(favourites_count)
        print(data)
        response =[]
        for i in data :
            song = i.song_data
            rating = format((song.rating_sum/song.count),'.2f')
            response.append({
                "id" : song.song_id,
                "name" : song.song_name,
                "genre" : song.genre,
                "singer_name" : song.creator_data.username,
                "releaseDate":song.release_date,
                "playbackCount":song.playback_count,
                "rating":rating,
                "duration":song.duration,
                "favorited_on" : i.favorited_on
            })
        return response
    
    @jwt_required()
    def post(self):
        user_data = get_jwt_identity()
        args = self.parser.parse_args()
        song_id = args['song_id']
        try :
            data = Songs.query.filter_by(song_id = song_id).one()
            if Favourites.query.filter_by(user_id = user_data['data']['user_id'],song_id = song_id).first():
                return {
                    "msg":"Song already in favourites",
                    "success":False
                },400
            fav = Favourites(user_id = user_data['data']['user_id'],song_id = song_id)
            db.session.add(fav)
            db.session.commit()
            return {
                "msg":"Song added to favourites",
                "success":True
            }
        

        except:
            return {
                "msg":"Invalid Song ID"
            },400
            

            