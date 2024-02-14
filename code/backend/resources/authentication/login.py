from flask_restful import Resource, reqparse, marshal_with, fields
from models.models import UserInfo
from bcrypt import checkpw
from flask_jwt_extended import create_access_token


output_fields={
    "msg": fields.String,
    "token":fields.String
}

class Login(Resource):

    def __init__(self) -> None:

        self.parser=reqparse.RequestParser()
        self.parser.add_argument("username", type=str, required=True)
        self.parser.add_argument("password",type=str,required=True)

    @marshal_with(output_fields)
    def post(self):

        args=self.parser.parse_args()
        username=args["username"]
        password=args["password"].encode('utf8')

        userCredentials=UserInfo.query.filter_by(username=username).first()
        if userCredentials==None:
            return {
            "msg":"username doesn't exist",
            "token":None
        },401

        if not(checkpw(password,userCredentials.password)):
            return {
            "msg":"Invalid username or password",
            "token":None
        },401

        token=create_access_token(identity=username)
        return {
            "msg":"Login Successful",
            "token":token
        },200