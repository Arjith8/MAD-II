from flask_restful import Resource, reqparse
from models.models import UserInfo
# import sqlalchemy
class Login(Resource):

    def __init__(self) -> None:

        self.parser=reqparse.RequestParser()
        self.parser.add_argument("username", type=str, required=True)
        self.parser.add_argument("password",type=str,required=True)

    def post(self):

        args=self.parser.parse_args()
        username=args["username"]
        password=args["password"]

        userCredentials=UserInfo.query.filter_by(username=username).first()
        if userCredentials.password==password:
            return "hi"

        return [password,username]
