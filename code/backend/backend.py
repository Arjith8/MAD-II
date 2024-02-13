from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from resources.authentication.login import Login
from models.models import db 


app = Flask(__name__)
api=Api(app)

app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///projectDB.sqlite3"

db.init_app(app)
app.app_context().push()


api.add_resource(Login,'/api/login')

if __name__=="__main__":
    app.run(debug=True)