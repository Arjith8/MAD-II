from flask_restful import Resource, reqparse
from flask_mail import Message

class mailClientForUser(Resource):
    def __init__(self) :
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('emails', type=list, required=True)
    def post(self):
        args = self.parser.parse_args()
        
        for i in args['emails']:
            # msg = Message(,