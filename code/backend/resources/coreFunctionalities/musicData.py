from flask_restful import Resource,reqparse, fields, marshal_with
from resources.models import Songs


data_format={
    "song_id":fields.Integer,
    "singerName":fields.String,
    "genre":fields.String,
    "releaseDate":fields.DateTime,
    "playbackCount":fields.Integer,
    "rating":fields.Float,
    "duration":fields.Float
}

response_fields=fields.List(fields.Nested(data_format))


class IndexData(Resource):
    def __init__(self):
        self.parser=reqparse.RequestParser()
        self.parser.add_argument('token',location="headers")

        
    # @marshal_with(response_fields)
    def get(self):
        response=[]
        data=Songs.query.order_by(Songs.playback_count.desc()).all()

        for i in data:
            rating = format((i.rating_sum/i.count),'.2f')
            response.append({
                "song_id":i.song_id,
                "singerName":i.creator_info.username,
                "genre":i.genre,
                "releaseDate":i.release_date,
                "playbackCount":i.playback_count,
                "rating":rating,
                "duration":i.duration
            })
        print(response)