from flask import Flask
from flask_restful import  Api
from flask_cors import CORS
from resources.authentication.login import Login
from resources.authentication.signup import SignUp
from resources.coreFunctionalities.musicData import IndexData
from resources.models import db 
from dotenv import dotenv_values
from flask_jwt_extended import JWTManager

app = Flask(__name__)
api=Api(app,prefix='/api/v1')

CORS(
    app,
    origins='http://localhost:5173'
)

env_vars=dotenv_values(".env")

sqliteUri=env_vars.get("SQLiteURI")
app.config['SQLALCHEMY_DATABASE_URI']=f"sqlite://{sqliteUri}"
db.init_app(app)
app.app_context().push()

jwt_key=env_vars.get("JWT_KEY")
app.config["JWT_SECRET_KEY"] = jwt_key
JWTManager(app)


api.add_resource(Login,'/login')
api.add_resource(SignUp,'/signup')
api.add_resource(IndexData,'/data')


debug=env_vars.get("DEBUG")
if __name__=="__main__":
    app.run(debug=debug)