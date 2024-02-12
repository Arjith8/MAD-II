from flask_restful import Resource,reqparse, output_json
from models.models import UserInfo

class SignUp(Resource):
    def __init__(self):
        self.parser=reqparse.RequestParser()
        self.parser.add_argument("username",type=str,required=True)
        self.parser.add_argument("password",type=str,required=True)
        self.parser.add_argument("first_name",type=str,required=True)
        self.parser.add_argument("last_name",type=str,required=True)

    def signup(self):
        args=self.parser.parse_args()
        username=args["username"]
        password=args["password"]
        first_name=args["first_name"]
        last_name=args["last_name"]

        if UserInfo.query.filter_by(username=username).first() !=None:
            return 

