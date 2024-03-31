from flask import Flask, render_template, request
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
from src.rate import rate
from database.models import db, UserInfo, Songs
from src.flag import flag
from src.playlist import Playlist
from src.dashboard.creatorDashboard import CreatorDashboard
from src.dashboard.adminDashboard import AdminDashboard
from src.song import Song
from src.search import search
from sqlalchemy import text
from cache_config import cache

# from src.lyrics import lyrics



app = Flask(__name__)
api=Api(app,prefix='/api/v1')
mail = Mail(app)
cache.init_app(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'arjithar.11a.svn@gmail.com'
app.config['MAIL_PASSWORD'] = 'cooc ewko ehbp gfpw'
app.config['MAIL_USE_TLS'] = True

app.config['MAIL_DEFAULT_SENDER'] = "arjithar.11a.svn@gmail.com"

mail = Mail(app)

CORS(
    app,
    origins='http://localhost:5173'
)

@app.route('/', methods=['GET', 'POST'])
def mail_server():
    data = request.get_json()
    emails = data['emails']
    for email in emails:
        purpose = data['purpose']
        if purpose == 'user_remainder':
            user_data = UserInfo.query.filter_by(email=email).first()
            songs = Songs.query.order_by(Songs.playback_count.desc()).limit(10)
            html = render_template('user_mail_template.html',username = user_data.username, songs=songs)
            message = Message(subject='Top 10 songs of the week', recipients=[email], html=html)
            mail.send(message)
            return "Mail sent successfully"
        
        if purpose == 'creator_remainder':
            user_data = UserInfo.query.filter_by(email=email).first()
            songs = db.session.execute(text(f"""select song_name, genre, release_date, playback_count, round(cast(rating_sum as real)/nullif(count,0),2) as rating from songs join user_info on songs.singer_id=user_info.user_id
                            where email = '{email}'
                            order by rating DESC;""")).fetchall()
            
            html = render_template('creator_mail_template.html',username = user_data.username, songs=songs)
            message = Message(subject='Monthly Creator Report', recipients=[email], html=html)
            mail.send(message)
            return "Mail sent successfully"




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
api.add_resource(SongData, '/song','/songs')
api.add_resource(favourites,'/favourites')
api.add_resource(upgradeToCreator,'/creator_upgrade')
api.add_resource(fetchCreator,'/creator','/creators')
api.add_resource(fetchAlbum,'/album','/albums')
api.add_resource(userData,'/user_data')
api.add_resource(lyrics,'/lyrics')
api.add_resource(rate,'/rate')
api.add_resource(flag,'/flag')
api.add_resource(Playlist, '/playlists','/playlist')
api.add_resource(CreatorDashboard, '/creator_dashboard')
api.add_resource(AdminDashboard, '/admin_dashboard')
api.add_resource(Song,'/song_operation')
api.add_resource(search,'/search')

# api.add_resource()


debug=env_vars.get("DEBUG")
if __name__=="__main__":
    app.run(debug=debug)