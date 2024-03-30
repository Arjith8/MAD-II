from flask_restful import Resource
from database.models import db, Songs, Albums, UserInfo
from flask import request
from sqlalchemy import text

class search(Resource):

    
    def get(self):
        print("search")
        keyword = request.args.get('keyword')
        try:
            rating = float(keyword)
            print(rating)
            data = db.session.execute(text(f"select song_id, song_name, cast(rating_sum as REAL)/nullif(count,0) as rating from songs where rating >= {rating}")).fetchall()
            return {
                "rating_based":True,
                "songs":[{
                    "song_id":i[0],
                    "song_name":i[1],
                    "rating":i[2]
                } for i in data],
                "albums":[],
                "creators":[]
            }
        except:
            data = Songs.query.filter(Songs.song_name.ilike(f"%{keyword}%")).all()
            songs = [{
                "song_id":i.song_id,
                "song_name":i.song_name,
            } for i in data]

            data = Albums.query.filter(Albums.album_name.ilike(f"%{keyword}%")).all()
            albums = [{
                "album_id":i.album_id,
                "album_name":i.album_name,
            } for i in data]

            data = UserInfo.query.filter(UserInfo.account_type=='creator', UserInfo.username.ilike(f"%{keyword}%")).all()
            creators = [{
                "creator_id":i.user_id,
                "creator_name":i.username
            } for i in data]

            return {
                "rating_based":False,
                "songs":songs,
                "albums":albums,
                "creators":creators
            }

        



        #     pass
