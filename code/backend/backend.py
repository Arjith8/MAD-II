from flask import Flask, request
from flask_restful import Resource, Api
from resources.authentication.login import Login
from resources.authentication.signup import SignUp
from models.models import db 
from dotenv import dotenv_values
from flask_jwt_extended import JWTManager

app = Flask(__name__)
api=Api(app)

env_vars=dotenv_values(".env")

sqliteUri=env_vars.get("SQLiteURI")
app.config['SQLALCHEMY_DATABASE_URI']=f"sqlite://{sqliteUri}"
db.init_app(app)
app.app_context().push()

jwt_key=env_vars.get("JWT_KEY")
app.config["JWT_SECRET_KEY"] = jwt_key
JWTManager(app)


api.add_resource(Login,'/api/login')
api.add_resource(SignUp,'/api/signup')


debug=env_vars.get("DEBUG")
if __name__=="__main__":
    app.run(debug=debug)