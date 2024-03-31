from flask_restful import Resource,reqparse, fields, marshal
from flask import request
from database.models import Songs, db
from cache_config import cache


response_type={
    "id":fields.Integer,
    "name":fields.String,
    "singer_name":fields.String,
    "genre":fields.String,
    "release_date":fields.String,
    "playback_count":fields.Integer,
    "lyrics":fields.String,
    "rating":fields.String,
    "duration":fields.Float,
}

invalid_response ={
    "msg" : fields.String
}

class SongData(Resource):
    def __init__(self):
        self.parser=reqparse.RequestParser()
        self.parser.add_argument('song_id',type=int, location='args')
        self.parser.add_argument('song_count',type=int,location='args')
    
    # @cache.cached(timeout=60, key_prefix=lambda: request.url)
    def get(self):

        args = self.parser.parse_args()
        if 'songs' in request.url:
            response = []
            if not args['song_count']:
                data=Songs.query.order_by(Songs.playback_count.desc()).limit(5)
            else:
                data=Songs.query.order_by(Songs.playback_count.desc()).limit(args['song_count'])
            for i in data:
                if i.count!=0:
                    rating = format((i.rating_sum/i.count),'.2f')
                else:
                    rating = None
                response.append({
                    "id":i.song_id,
                    "name":i.song_name,
                    "singer_name":i.creator_data.username,
                    "genre":i.genre,
                    "release_date":i.release_date,
                    "playback_count":i.playback_count,
                    "rating":rating,
                    "duration":i.duration,
                    "flags":len(i.song_flags),
                })
            return response,200

        if not args["song_id"]:
            return {
                "msg":"Song ID was not provided"
            },400
        
        song_id = args['song_id']
        song = Songs.query.filter_by(song_id=song_id).first()

        if not(song):
            data =  {
                "msg" : "Invalid Song ID"
            }
            response = marshal(data,invalid_response)
            return response,400
        
        if song.count!=0:
            rating = format((song.rating_sum/song.count),'.2f')
        else:
            rating = None

        with(open(f"/mnt/c/New folder (2)/MAD-II/code/frontend/public/lyrics/{song.song_id}.txt",'r')) as f:
            lyrics = f.read()
        data = {
            "id":song.song_id,
            "name":song.song_name,
            "singer_name":song.creator_data.username,
            "genre":song.genre,
            "release_date":song.release_date,
            "playback_count":song.playback_count,
            "rating":rating,
            "lyrics":lyrics,
            "duration":song.duration,
            "flags":len(song.song_flags)
        }
        response = marshal(data,response_type)
        song.playback_count+=1
        db.session.commit()
        return response
    
    