from flask_restful import Resource,reqparse, marshal_with, fields
from datetime import timedelta
from datetime import datetime
from bcrypt import gensalt, hashpw
from flask_jwt_extended import create_access_token
from database.models import UserInfo
from database.models import db

response_fields={
    "msg":fields.String,
    "token":fields.String
}

class SignUp(Resource):
    def __init__(self):
        self.parser=reqparse.RequestParser()
        self.parser.add_argument("username",type=str,required=True)
        self.parser.add_argument("password",type=str,required=True)
        self.parser.add_argument("first_name",type=str,required=True)
        self.parser.add_argument("last_name",type=str,required=True)
        self.parser.add_argument("email",type=str,required=True)

    @marshal_with(response_fields)
    def post(self):
        args=self.parser.parse_args()
        username=args["username"]
        password=args["password"].encode('utf8')
        first_name=args["first_name"]
        last_name=args["last_name"]
        email = args["email"]

        if UserInfo.query.filter_by(username=username).first() !=None:
            return {
                "msg":"Username already exists! Try another one",
                "token":None
            }
        
        password=hashpw(password,gensalt())
        sign_up_date=datetime.now().strftime("%Y-%m-%d")
        last_seen=datetime.now().strftime("%Y-%m-%d")

        data=UserInfo(username=username,password=password,first_name=first_name,last_name=last_name,sign_up_date=sign_up_date,last_seen=last_seen, email=email)
        db.session.add(data)
        db.session.commit()
        token=create_access_token(identity={
            "data":{
                "user_id" : data.user_id,
                "user_type" : "Normal"
            }
        },expires_delta=timedelta(days=1))
        return {
            "msg":"User created successfully",
            "token":"Bearer "+token,
        }

