from flask_restful import Resource, reqparse, marshal_with, fields
from datetime import timedelta
from database.models import UserInfo
from database.models import AdminInfo
from bcrypt import checkpw
from flask_jwt_extended import create_access_token
from bcrypt import checkpw

output_fields={
    "msg": fields.String,
    "token":fields.String,
    "user_type":fields.String
}


class Login(Resource):

    def __init__(self) -> None:

        self.parser=reqparse.RequestParser()
        self.parser.add_argument("username", type=str, required=True, help = "Username was not send")
        self.parser.add_argument("password",type=str,required=True, help = "Password was not send")
        self.parser.add_argument("user_type")

    @marshal_with(output_fields)
    def post(self):

        args=self.parser.parse_args()
        username=args["username"].encode('utf-8')
        password=args["password"].encode('utf-8')
        if args['user_type'] == "Admin":
            user_type = "Admin"
            userCredentials = AdminInfo.query.first()
            if checkpw(username,userCredentials.admin_username):
                if not(checkpw(password,userCredentials.password)):
                    return {
                        "message":"Unauthorized",
                    },401
                return {
                    "message":"Login Successful",
                    "token":"Bearer "+create_access_token(identity={
                        "data":{
                            "user_id":userCredentials.admin_id,
                            "user_type":user_type
                        }
                    },expires_delta=timedelta(days=1)),
                    "valid_username":True
                },200
                
        else:
            userCredentials=UserInfo.query.filter_by(username=username).first()
            user_type = userCredentials.account_type
            
        if userCredentials==None:
           return {
            "msg":"Invalid username or password",
            "token":None,
        },401

        if not(checkpw(password,userCredentials.password)):
            return {
            "msg":"Invalid username or password",
            "token":None,
        },401
        
        token=create_access_token(identity={
            "data":{
                "user_id" : userCredentials.user_id,
                "user_type" : user_type
            }
        },expires_delta=timedelta(days=1))
        return {
            "msg":"Login Successful",
            "token":"Bearer "+token,
            "valid_username":True
        },200