from flask_restful import Resource, reqparse
from flask_jwt_extended import decode_token

def token_validator(token):
    if token:
        data=decode_token(token)
        