from flask_restful import Resource, reqparse
from database.models import Lyrics, db
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime
from flask import request

class lyrics(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("lyrics_id", location = 'args')
        self.parser.add_argument("lyrics_name", type = str )
        self.parser.add_argument("lyrics", type = str)

    
    def get(self):
        args = request.args
        data = Lyrics.query.filter_by(lyrics_id = args['lyrics_id']).first()
        lyrics = ''
        with open(f"C:/New folder (2)/MAD-II/code/frontend/public/raw_lyrics/{data.lyrics_id}.txt", "r") as f:
            lyrics = f.read()

        if not data:
            return {
                "msg":"Lyrics not found",
                "success":False
            }
        
        return {
            "lyrics_id":data.lyrics_id,
            "creator_id":data.creator_id,
            "creator_name":data.creator_data.username,
            "lyrics_name":data.lyrics_name,
            "release_date":data.release_date,
            "lyrics":lyrics,
            "success":True
        }
    
    @jwt_required()
    def post(self):
        args = self.parser.parse_args()
        if args['lyrics_name'] == None or args['lyrics'] == None:
            return {
                "msg":"Lyrics name or lyrics not provided",
                "success":False
            }
        user_data = get_jwt_identity()
        if user_data['data']['user_type'] != "creator":
            return {
                "msg":"Update to creator account to add lyrics",
                "success":False
            }
        data = Lyrics.query.filter_by(lyrics_name = args['lyrics_name']).first()
        if data:
            return {
                "msg":"Lyrics already exists",
                "success":False
            }
        release_date = datetime.now().strftime("%Y-%m-%d")
        print(user_data['data']['user_id'])
        data = Lyrics(lyrics_name = args['lyrics_name'], release_date = release_date, creator_id = user_data['data']['user_id'])
        db.session.add(data)
        db.session.commit()
        with open(f"C:/New folder (2)/MAD-II/code/frontend/public/raw_lyrics/{data.lyrics_id}.txt", "w") as f:
            f.write(args['lyrics'])
        
        return {
            "msg":"Lyrics added successfully",
            "success":True
        }
    
    @jwt_required()
    def put(self):
        args = self.parser.parse_args()
        user_data = get_jwt_identity()
        print(args)
        data = Lyrics.query.filter_by(lyrics_id = args['lyrics_id'], creator_id = user_data['data']['user_id']).first()
        if not data:
            return {
                "msg":"Lyrics not found",
                "success":False
            }
        if data.lyrics_name != args['lyrics_name']:
            data.lyrics_name = args['lyrics_name']
        with open(f"C:/New folder (2)/MAD-II/code/frontend/public/raw_lyrics/{data.lyrics_id}.txt", "w") as f:
            f.write(args['lyrics'])
        db.session.commit()
        return {
            "msg":"Lyrics updated successfully",
            "success":True
        }
    
    @jwt_required()
    def delete(self):
        id = request.args.get('lyrics_id')
        user_data = get_jwt_identity()
        data = Lyrics.query.filter_by(lyrics_id = id, creator_id = user_data['data']['user_id']).first()
        if not data:
            return {
                "msg":"Lyrics not found",
                "success":False
            }
        db.session.delete(data)
        db.session.commit()
        return {
            "msg":"Lyrics deleted successfully",
            "success":True
        }