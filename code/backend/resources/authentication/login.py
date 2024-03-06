from flask_restful import Resource, reqparse, marshal_with, fields
from resources.models import UserInfo
from bcrypt import checkpw
from flask_jwt_extended import create_access_token

output_fields={
    "msg": fields.String,
    "token":fields.String,
    "valid_username":fields.Boolean
}


class Login(Resource):

    def __init__(self) -> None:

        self.parser=reqparse.RequestParser()
        self.parser.add_argument("username", type=str, required=True)
        self.parser.add_argument("password",type=str,required=True)

    @marshal_with(output_fields)
    def post(self):

        args=self.parser.parse_args()
        print(args)
        username=args["username"]
        password=args["password"].encode('utf8')

        userCredentials=UserInfo.query.filter_by(username=username).first()
        if userCredentials==None:
            return {
            "msg":"username doesn't exist, would you like to register as a new user ",
            "token":None,
            "valid_username":False
        },401

        if not(checkpw(password,userCredentials.password)):
            return {
            "msg":"Invalid username or password",
            "token":None,
            "valid_username":True

        },401
        
        token=create_access_token(identity=userCredentials.user_id)
        return {
            "msg":"Login Successful",
            "token":token,
            "valid_username":True
        },200