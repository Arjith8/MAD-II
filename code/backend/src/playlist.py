from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import request
from database.models import Playlists, PlaylistSongs, Songs, db
from flask import request


class Playlist(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('playlist_id', type=int, location='args')
        self.parser.add_argument("token", type=str, location='headers')
        self.parser.add_argument("playlist_name", type=str, location='body')
        self.parser.add_argument("song_id", type=int, location='body')
        self.parser.add_argument("image", type=str, location='body')

    @jwt_required()
    def get(self):
        args = self.parser.parse_args()
        user_data = get_jwt_identity()
        user_id = user_data['data']['user_id']

        if 'playlists' in request.url:
            data = Playlists.query.filter_by(user_id=user_id).all()
            response = []
            for playlist in data:
                songs = playlist.playlist_songs_id
                print(songs[0].song_data)

                response.append({
                    "id": playlist.playlist_id,
                    "name": playlist.playlist_name,
                    "songs": [{
                        "song_id": i.song_data.song_id,
                        "song_name": i.song_data.song_name,
                        "release_date": i.song_data.release_date,
                        "playback_count": i.song_data.playback_count,
                        "rating": format((i.song_data.rating_sum / i.song_data.count), '.2f'),
                        "duration": i.song_data.duration,
                    } for i in songs]})
            return response
        

        playlist_id = args['playlist_id']

        if not playlist_id:
            return {"message": "playlist_id is required"}, 400
        
        data = Playlists.query.filter_by(playlist_id=playlist_id, user_id=user_id).first()

        if not data:
            return {"message": "Playlist not found"}, 404
        songs = data.playlist_songs_id

        return {
            "id": data.playlist_id,
            "name": data.playlist_name,
            "songs": [{
                "song_id": i.song_id,
                "song_name": i.song_data.song_name,
                "release_date": i.song_data.release_date,
                "playback_count": i.song_data.playback_count,
                "rating": format((i.song_data.rating_sum / i.song_data.count), '.2f'),
                "duration": i.song_data.duration,
            } for i in songs]
        }
    
    @jwt_required()
    def post(self):
        user_data = get_jwt_identity()
        user_id = user_data['data']['user_id']

        playlist_name = request.form.get('playlist_name')
        songs = request.form.getlist('songs')
        songs = songs[0].split(',')
        thumbnail = request.files.get('thumbnail')

        if not playlist_name or not songs or thumbnail is None:
            return {"message": "Invalid request"}, 400

        if Playlists.query.filter_by(user_id=user_id, playlist_name=playlist_name).first():
            return {
                "message": "Playlist already exists",
                "success":False
            }, 400
        playlist = Playlists(user_id=user_id, playlist_name=playlist_name)
        db.session.add(playlist)
        db.session.commit()
        for song in songs:
            if song:
                print(playlist.playlist_id, song)
                song_id = Songs.query.filter_by(song_name=song).first().song_id
                playlist_song = PlaylistSongs(playlist_id=playlist.playlist_id, song_id=song_id)
                db.session.add(playlist_song)
                db.session.commit()
        thumbnail.save(f"C:/New folder (2)/MAD-II/code/frontend/public/playlist/{playlist.playlist_id}.jpg")
        

        
        return {
            "message": "Playlist created successfully",
            "success": True
            }, 201

