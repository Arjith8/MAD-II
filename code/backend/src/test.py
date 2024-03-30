from flask_restful import Resource
from database.models import UserInfo, Songs,Albums, db
from flask_jwt_extended import jwt_required, get_jwt_identity
from sqlalchemy import text
from datetime import datetime


class fetch(Resource):
    @jwt_required()
    def get(self):
        user_data = get_jwt_identity()
        if user_data['data']['user_type'] != 'Admin':
            return {
                "message": "Access Denied"
            }, 401
        
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

        songs_in_order_of_popularity = db.session.execute(text("SELECT song_id,song_name,release_date, round(cast(rating_sum as Real)/NULLIF(count,0),2) as rating FROM songs order by rating desc")).fetchall()
        best_song = songs_in_order_of_popularity[0]
        print(best_song)

        creators_in_order_of_popularity = db.session.execute(text("""SELECT u.username,
                                                                count(s.song_id) ,
                                                                round(max(cast(s.rating_sum as Real)/nullif(s.count,0)),2),
                                                                s.song_name, 
                                                                s.song_id, round(sum(cast(s.rating_sum as Real))/sum(s.count),2) as rating
                                                                from user_info as u INNER JOIN songs s on u.user_id=s.singer_id 
                                                                GROUP by s.singer_id ORDER by rating desc;""")).fetchall()
        
        best_creator = creators_in_order_of_popularity[0]
        
        song_count = len(Songs.query.all())
        creator_count = len(creators_in_order_of_popularity)
        albums_count = len(Albums.query.all())


        return {
            "user_retention": user_retention,
        }



