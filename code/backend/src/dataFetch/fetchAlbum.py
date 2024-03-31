from flask_restful import Resource, reqparse, marshal, fields
from database.models import Albums, db, AlbumSongs, Songs
from cache_config import cache
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import request

song_data_type = {
    "song_id":fields.Integer,
    "song_name":fields.String,
    "release_date":fields.String,
    "playback_count":fields.Integer,
    "rating":fields.Float,
    "duration":fields.Float,
}

response_type = {"id" : fields.Integer,
    "name" : fields.String,
    "genre":fields.String,
    "songs" : fields.List(fields.Nested(song_data_type))
}

class fetchAlbum(Resource):

    def __init__(self) :
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('album_id',type=int, location='args')
        self.parser.add_argument('album_count',type=int,location='args')

    @cache.cached(timeout=60, key_prefix=lambda: request.url)
    def get(self):
        args = self.parser.parse_args()
        if '/albums' in request.url:
            album_count = args['album_count']
            if not album_count:
                album_count = 5
            data = Albums.query.limit(album_count)
            response = []
            for album in data:
                songs = album.songs
                response.append({
                    "id" : album.album_id,
                    "name" : album.album_name,
                    "genre":album.genre,
                    "songs" : [{
                        "song_id":i.song_id,
                        "song_name":i.song_data.song_name,
                        "release_date":i.song_data.release_date,
                        "playback_count":i.song_data.playback_count,
                        "rating":format((i.song_data.rating_sum/i.song_data.count),'.2f'),
                        "duration":i.song_data.duration,
                    }for i in songs]})
            return response
        
        if not args['album_id']:
            return {
                "msg":"Album ID was not provided"
            },400
        try:

            data = Albums.query.filter(Albums.album_id==args['album_id']).one()
            print(data)
            songs = data.songs
            
            return marshal({
                "id" : data.album_id,
                "name" : data.album_name,
                "genre":data.genre,
                "songs" : [{
                    "song_id":i.song_id,
                    "song_name":i.song_data.song_name,
                    "release_date":i.song_data.release_date,
                    "playback_count":i.song_data.playback_count,
                    "rating":format((i.song_data.rating_sum/i.song_data.count),'.2f') if i.song_data.count != 0 else None,
                    "duration":i.song_data.duration,
                }for i in songs]
            },response_type)

        except:
            return {
                "msg":"Invalid Album ID"
            }
        
    @jwt_required()
    def post(self):
        user_data = get_jwt_identity()
        user_id = user_data['data']['user_id']

        album_name = request.form.get('album_name')
        genre = request.form.get('genre')
        songs = request.form.getlist('songs')
        songs = songs[0].split(',')
        thumbnail = request.files.get('thumbnail')
        # print(thumbnail, songs, album_name, genre)

        if not album_name or not songs or thumbnail is None:
            return {"message": "Invalid request"}, 400

        if Albums.query.filter_by(singer_id=user_id, album_name=album_name).first():
            return {
                "message": "Album already exists",
                "success":False
            }, 400
        album = Albums(singer_id=user_id, album_name=album_name, genre=genre)
        db.session.add(album)
        db.session.commit()
        # print(songs)
        song_ids = []
        for i in songs:
            song = Songs.query.filter_by(song_name=i, singer_id = user_id).first()
            if song:
                song_ids.append(song.song_id)
        if song_ids:
            for i in song_ids:
                album_song = AlbumSongs(album_id=album.album_id, song_id=i)
                db.session.add(album_song)
                db.session.commit()
        else:
            db.session.delete(album)
            db.session.commit()
            return {
                "message": "No songs found, aborting album creation",
                "success":False
            }, 400
        thumbnail.save(f"/mnt/c/New folder (2)/MAD-II/code/frontend/public/album/{album.album_id}.jpg")
        return {
            "message": "Album created successfully",
            "success":True
        }, 200
    
    @jwt_required()
    def put(self):
        user_data = get_jwt_identity()
        user_id = user_data['data']['user_id']
        album_id = request.form.get('album_id')
        album_name = request.form.get('album_name')
        genre = request.form.get('genre')
        songs = request.form.getlist('songs')
        songs = songs[0].split(',')
        thumbnail = request.files.get('thumbnail')

        if not album_name or not songs :
            return {"message": "Invalid request"}, 400
        
        album = Albums.query.filter_by(album_id=album_id, singer_id=user_id).first()
        if not album:
            return {"message": "Invalid album id"}, 400
        album.album_name = album_name
        album.genre = genre
        db.session.commit()
        album_songs = AlbumSongs.query.filter_by(album_id=album_id).all()
        for i in album_songs:
            db.session.delete(i)
            db.session.commit()
        song_ids = []
        for i in songs:
            song = Songs.query.filter_by(song_name=i, singer_id = user_id).first()
            if song:
                song_ids.append(song.song_id)
        if song_ids:
            for i in song_ids:
                album_song = AlbumSongs(album_id=album.album_id, song_id=i)
                db.session.add(album_song)
                db.session.commit()
        if thumbnail:
            thumbnail.save(f"/mnt/c/New folder (2)/MAD-II/code/frontend/public/album/{album.album_id}.jpg")
        return {
            'message': 'Album updated successfully',
            'success':True
        }
         
    
    @jwt_required()
    def delete(self):
        user_data = get_jwt_identity()
        user_id = user_data['data']['user_id']
        print(user_data)
        album_id = self.parser.parse_args()['album_id']
        if not album_id:
            return {"message": "Invalid request"}, 400
        if user_data['data']['user_type'] == 'Admin':
            album = Albums.query.filter_by(album_id=album_id).first()
            print("hi")

            album_songs = AlbumSongs.query.filter_by(album_id=album_id).all()
            for i in album_songs:
                db.session.delete(i)
                db.session.commit()
            db.session.delete(album)
            db.session.commit()
            return {"message": "Album deleted successfully","success":True}, 200
        album = Albums.query.filter_by(album_id=album_id, singer_id=user_id).first()
        if not album:
            return {"message": "Invalid album id"}, 400
        album_songs = AlbumSongs.query.filter_by(album_id=album_id).all()
        for i in album_songs:
            db.session.delete(i)
            db.session.commit()

        db.session.delete(album)
        db.session.commit()
        return {"message": "Album deleted successfully","success":True}, 200

        
        
