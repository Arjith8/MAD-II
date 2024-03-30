from flask_restful import Resource
from database.models import UserInfo, Songs,Albums, db
from sqlalchemy import text
from datetime import datetime


class AdminDashboard(Resource):
    def get(self):
        data = UserInfo.query.all()
        total_users = len(data)
        total_active_users = 0
        current_date = datetime.now()
        for i in data :
            last_seen_difference = current_date-datetime.strptime(i.last_seen,'%Y-%m-%d')
            if last_seen_difference.days < 30:
                total_active_users += 1
        if total_users != 0:
            user_retention = total_active_users/total_users*100
        else:
            user_retention = None

        songs_in_order_of_popularity = db.session.execute(text("SELECT song_id,song_name,release_date, round(cast(rating_sum as Real)/NULLIF(count,0),2) as rating,singer_id, username, playback_count FROM songs join user_info on user_id=singer_id order by rating desc")).fetchall()
        songs = [{
            "song_id": song[0],
            "song_name": song[1],
            "release_date": song[2],
            "rating": song[3],
            "singer_id": song[4],
            "singer_name": song[5],
            "playback_count": song[6]
        } for song in songs_in_order_of_popularity]

       

        creators_in_order_of_rating = db.session.execute(text("""SELECT u.username,
                count(s.song_id) as song_count,
                round(max(cast(s.rating_sum as Real)/nullif(s.count,0)),2) as max_rating,
                s.song_name, 
                s.song_id, round(sum(cast(s.rating_sum as Real))/sum(s.count),2) as rating,
                sum(s.playback_count) as total_playback_count,
                s.singer_id
                from user_info as u INNER JOIN songs s on u.user_id=s.singer_id 
                GROUP by s.singer_id ORDER by rating desc;""")).fetchall()
        
        albums_in_order_of_popularity = db.session.execute(text("""select j.album_id,j.album_name,username, j.singer_id,j.song_id,j.song_name, genre, sum(playback_count) as playback_count, round(avg(rating),2) from user_info join (select i.album_id,i.singer_id,i.song_id, song_name, i.genre, playback_count, album_name, CAST(rating_sum as real)/nullif(songs.count,0)as rating from songs join 
(select albums.album_id, singer_id, album_name, genre, song_id from albums join album_songs on albums.album_id=album_songs.album_id) as i
on songs.song_id=i.song_id) as j on j.singer_id=user_info.user_id group by album_id order by playback_count desc""")).fetchall()
        
        print(albums_in_order_of_popularity[0])
        
        albums=[{
            "album_id": album[0],
            "album_name": album[1],
            "singer_id": album[3],
            "singer_name": album[2],
            "genre": album[6],
            "total_playbacks": album[7],
            "average_rating": album[8]
        } for album in albums_in_order_of_popularity]
        print(albums[0])
        
        creators = [{
            "username": creator[0],
            "song_count": creator[1],
            "max_rating": creator[2],
            "best_song": creator[3],
            "best_song_id": creator[4],
            "average_rating": creator[5],
            "total_playback_count": creator[6],
            "singer_id":creator[7]
        } for creator in creators_in_order_of_rating]

        


        return {
            "user_retention": user_retention,
            "songs": songs,
            "creators":creators,
            "albums":albums
        }

