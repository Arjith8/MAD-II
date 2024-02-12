from flask_restful import Resource, reqparse

class Login(Resource):

    def __init__(self) -> None:

        self.parser=reqparse.RequestParser()
        self.parser.add_argument("username", type=str, required=True)
        self.parser.add_argument("password",type=str,required=True)

    def post(self):
        args=self.parser.parse_args()
        return args
        pass
