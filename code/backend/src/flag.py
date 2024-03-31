from flask_restful import Resource, reqparse
from database.models import SongFlags, db, Songs
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy import text

class flag(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("song_id", required=True, type = int, location='args')

    @jwt_required()
    def get(self):

        user_data = get_jwt_identity()
        print(user_data)
        if user_data['data']['user_type'] == 'Admin':
            songs = db.session.execute(text("""select songs.song_id, song_name, release_date, playback_count, flags from songs join (select song_id, count(user_id) as flags from song_flags GROUP by song_id)as f 
                on songs.song_id=f.song_id
                order by flags desc;"""))
            
            resp =  [{
                "song_id":song.song_id,
                "song_name":song.song_name,
                "release_date":song.release_date,
                "playback_count":song.playback_count,
                "flags":song.flags
            }for song in songs]

            return resp

    @jwt_required()
    def post(self):
        user_data = get_jwt_identity()
        args = self.parser.parse_args()
        
        try:
            data = SongFlags(song_id = args['song_id'], user_id = user_data['data']['user_id'])
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
