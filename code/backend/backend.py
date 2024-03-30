from flask import Flask, render_template
from flask_restful import  Api
from flask_cors import CORS
from dotenv import dotenv_values
from flask_jwt_extended import JWTManager
from flask_mail import Mail, Message

from src.authentication.login import Login
from src.authentication.signup import SignUp
from src.favourites import favourites
from src.upgradeToCreator import upgradeToCreator
from src.dataFetch.fetchCreator import fetchCreator
from src.dataFetch.fetchSong import SongData
from src.userData import userData
from src.dataFetch.fetchAlbum import fetchAlbum
from src.lyrics import lyrics
from src.test import fetch
from src.rate import rate
from database.models import db, UserInfo, Songs
from src.flag import flag
from src.playlist import Playlist
from src.dashboard.creatorDashboard import CreatorDashboard
from src.dashboard.adminDashboard import AdminDashboard
from src.song import Song
from src.search import search

# from src.lyrics import lyrics



app = Flask(__name__)
api=Api(app,prefix='/api/v1')
mail = Mail(app)
app.config['MAIL_SERVER'] = '172.20.136.64'
app.config['MAIL_PORT'] = 1025
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USERNAME'] = None
app.config['MAIL_PASSWORD'] = None
app.config['MAIL_DEFAULT_SENDER'] = 'arjithar.11a.svn@gmail.com'


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

@app.route('/user_mail_client/<string:email>')
def user_mail_client(email):
    print(email)
    user_data = UserInfo.query.filter_by(email=email).first()
    songs = Songs.query.order_by(Songs.playback_count.desc()).limit(10)

    html = render_template('user_mail_template.html',username = user_data.username, songs=songs)
    message = Message(subject='Top 10 songs of the week', recipients=[email], html=html)
    mail.send(message)
    return "Mail sent successfully"

    


api.add_resource(Login,'/login')
api.add_resource(SignUp,'/signup')
api.add_resource(SongData, '/song','/songs')
api.add_resource(favourites,'/favourites')
api.add_resource(upgradeToCreator,'/creator_upgrade')
api.add_resource(fetchCreator,'/creator','/creators')
api.add_resource(fetchAlbum,'/album','/albums')
api.add_resource(userData,'/user_data')
api.add_resource(lyrics,'/lyrics')
api.add_resource(rate,'/rate')
api.add_resource(flag,'/flag')
api.add_resource(fetch, '/test')
api.add_resource(Playlist, '/playlists','/playlist')
api.add_resource(CreatorDashboard, '/creator_dashboard')
api.add_resource(AdminDashboard, '/admin_dashboard')
api.add_resource(Song,'/song_operation')
api.add_resource(search,'/search')

# api.add_resource()


debug=env_vars.get("DEBUG")
if __name__=="__main__":
    app.run(debug=debug)