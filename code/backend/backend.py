from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api=Api(app)

class Login(Resource):
    def post(self):
        print(request.json["msg"])
        pass

api.add_resource(Login,'/api/login')
if __name__=="__main__":
    app.run(debug=True)