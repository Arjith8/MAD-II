from flask_restful import Resource, fields, marshal, reqparse
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask import request
from database.models import UserInfo, db

response_type = {
    "username" : fields.String,
    "first_name" : fields.String,
    "last_name" : fields.String,
    "account_type" : fields.String,
    "email": fields.String,
    "success": fields.Boolean
}

class userData(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("username")
        self.parser.add_argument("first_name")
        self.parser.add_argument("last_name")
        self.parser.add_argument("email")

    @jwt_required()
    def get(self):
        data = get_jwt_identity()
        user_id = data['data']["user_id"]
        user = UserInfo.query.filter_by(user_id=user_id).first()
        return marshal({
            "username":user.username,
            "first_name" : user.first_name,
            "last_name" : user.last_name,
            "account_type" : user.account_type,
            "email": user.email,
            "success":True
        },response_type)
    
    @jwt_required()
    def post(self):
        body = {}
        body["username"] = request.form.get('username')
        body["first_name"] = request.form.get("first_name")
        body["last_name"] = request.form.get('last_name')
        body["email"] = request.form.get('email')
        dp = request.files.get('dp')
        print(dp)
        data = get_jwt_identity()
        user_id = data['data']["user_id"]
        user = UserInfo.query.filter_by(user_id=user_id).first()
        if body['username']!=user.username:
            if UserInfo.query.filter_by(username=body['username']).first():
                return {
                    "msg":"username already exists",
                    "success":False
                },409
            user.username = body['username']
        user.first_name = body['first_name']
        user.last_name = body['last_name']
        user.email = body['email']
        db.session.commit()
        if dp:
            dp.save(f'/mnt/c/New folder (2)/MAD-II/code/frontend/public/creator/{user_id}.jpg')

        return {
            "success":True
        }
        