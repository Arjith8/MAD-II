from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from database.models import UserInfo, Songs, Albums, Lyrics


class CreatorDashboard(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
    @jwt_required()
    def get(self):
        user_data = get_jwt_identity()
        if UserInfo.query.filter_by(user_id=user_data['data']['user_id']).first().account_type != 'creator':
            return {"message": "You are not a creator"}, 400
        
        all_songs = Songs.query.order_by(Songs.playback_count.desc()).all()
        songs = []
        rank = []
        c=0
        for i in all_songs:
            c+=1
            if i.singer_id == user_data['data']['user_id']:
                rank.append(c)
                songs.append(i)

        # creators = 
        # print(songs)
        total_playback_counts = 0
        for i in songs:
            total_playback_counts += i.playback_count

        albums = Albums.query.filter_by(singer_id=user_data['data']['user_id']).all()
        # print(albums[0].songs.song_data)

        lyrics = Lyrics.query.filter_by(creator_id=user_data['data']['user_id']).all()
        
        
        return {
            "total_playback_count": total_playback_counts,
            "songs": [{
                "song_id": i.song_id,
                "song_name": i.song_name,
                "release_date": i.release_date,
                "genre": i.genre,
                "playback_count": i.playback_count,
                "rating": format((i.rating_sum / i.count), '.2f') if i.count != 0 else None,
                "duration": i.duration,
            } for i in songs],
            "ranks": rank,
            "albums": [{
                "album_id": i.album_id,
                "album_name": i.album_name,
                "genre": i.genre,
                "songs_count": len(i.songs),
            } for i in albums],
            "lyrics": [{
                "lyrics_id": i.lyrics_id,
                "lyrics_name": i.lyrics_name,
                "release_date": i.release_date,
            } for i in lyrics],
        }