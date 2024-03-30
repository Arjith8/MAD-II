from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from database.models import Songs,UserInfo, db
from flask import request
from datetime import datetime
from mutagen.mp3 import MP3


class Song(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('song_id', type=int)
        self.parser.add_argument('song_name', type=str)
        self.parser.add_argument('genre', type=str)
        self.parser.add_argument('lyrics', type=str)
        pass
    @jwt_required()
    def post(self):
        user_data = get_jwt_identity()
        song_name = request.form.get('song_name')
        genre = request.form.get('genre')
        lyrics = request.files.get('lyrics')
        song_mp3 = request.files.get('song')
        thumbnail = request.files.get('thumbnail')
        
        if Songs.query.filter_by(song_name=song_name).first():
            return {"message": "Song already exists", "success":False}, 400
        
        if UserInfo.query.filter_by(user_id=user_data['data']['user_id']).first().account_type != 'creator':
            return {"message": "You are not a creator", "success":False}, 401
        
        if not song_name or not genre or not lyrics or not song_mp3 or not thumbnail:
            return {"message": "All fields are required", "success":False}, 400
        
        release_date = datetime.now().strftime("%Y-%m-%d")
        song_duration = MP3(song_mp3).info.length

        song = Songs(singer_id=user_data['data']['user_id'], song_name=song_name, genre=genre, release_date=release_date, duration = song_duration)
        db.session.add(song)
        db.session.commit()
        lyrics.save(f"C:/New folder (2)/MAD-II/code/frontend/public/lyrics/{song.song_id}.txt")
        song_mp3.save(f"C:/New folder (2)/MAD-II/code/frontend/public/tracks/{song.song_id}.mp3")
        thumbnail.save(f"C:/New folder (2)/MAD-II/code/frontend/public/song/{song.song_id}.jpg")

        return {
            "message": "Song uploaded successfully",
            "success":True
        }
    
    @jwt_required()
    def put(self):
        args = self.parser.parse_args()
        user_data = get_jwt_identity()
        song_id = args['song_id']

        song = Songs.query.filter_by(singer_id=user_data['data']['user_id'], song_id=song_id).first()
        if not song:
            return {"message": "Song not found", "success":False}, 400
        
        song.song_name = args['song_name']
        song.genre = args['genre']
        with(open(f"C:/New folder (2)/MAD-II/code/frontend/public/lyrics/{song.song_id}.txt",'w')) as f:
            f.write(args['lyrics'])
        db.session.commit()
        return {
            "message": "Song updated successfully",
            "success":True
        }
        

    @jwt_required()
    def delete(self):
        args = self.parser.parse_args()
        song_id = args['song_id']
        user_data = get_jwt_identity()
        if user_data['data']['user_type'] == 'Admin':
            song = Songs.query.filter_by(song_id=song_id).first()
            print(song)
            if song:
                db.session.delete(song)
                db.session.commit()
                return {
                    "message": "Song deleted successfully",
                    "success":True
                }, 200
            return {
            "message": "Song deleteion failed",
            "success":False
        }

        if not song_id:
            return {"message": "Song ID is required", "success":False}, 400
        
        if Songs.query.filter_by(singer_id=user_data['data']['user_id'], song_id=song_id).first():
            song = Songs.query.filter_by(song_id=song_id).first()
            db.session.delete(song)
            db.session.commit()
            return {
                "message": "Song deleted successfully",
                "success":True
            }, 200
        
        return {
            "message": "Song deleteion failed",
            "success":False
        }
    
