from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class UserInfo(db.Model):

    user_id=db.Column(db.Integer,autoincrement=True,primary_key=True,nullable=False)
    first_name=db.Column(db.String(40),nullable=False)
    last_name=db.Column(db.String(40),nullable=False)
    username=db.Column(db.String(40),nullable=False,unique=True)
    password=db.Column(db.String(256),nullable=False)
    account_type=db.Column(db.String(10),nullable=False,default='normal')
    last_seen=db.Column(db.String,nullable=False)
    sign_up_date=db.Column(db.String,nullable=False)
    blacklisted=db.Column(db.Boolean,default=False)

    favourites=db.relationship("Favourites",backref="user_info")
    songs=db.relationship("Songs",backref="creator_info")
    albums=db.relationship("Albums",backref="creator_info")
    playlists=db.relationship("Playlists",backref="user_info")
    lyrics=db.relationship("Lyrics",backref="creator_info")

class Songs(db.Model):

    song_id=db.Column(db.Integer,nullable=False,autoincrement=True,primary_key=True)
    singer_id=db.Column(db.Integer,db.ForeignKey("user_info.user_id",ondelete="cascade"),nullable=False)
    song_name=db.Column(db.String,nullable=False,unique=True)
    genre=db.Column(db.String,nullable=False)
    release_date=db.Column(db.String,nullable=False)
    flags=db.Column(db.Integer,default=0)
    playback_count=db.Column(db.Integer,default=0)
    count=db.Column(db.Integer,default=0)
    rating_sum=db.Column(db.Integer)
    duration=db.Column(db.Integer)

    fav_by=db.relationship("Favourites",backref="song_data")
    albums=db.relationship("Albums",backref="song_data")
    playlists=db.relationship("Playlists",backref="song_data")

class Lyrics(db.Model):
    
    lyrics_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    creator_id=db.Column(db.Integer,db.ForeignKey("user_info.user_id",ondelete="cascade"))
    lyrics_name=db.Column(db.String,nullable=False)
    release_date=db.Column(db.String,nullable=False)
    rating_sum=db.Column(db.Integer,default=0)
    count=db.Column(db.Integer,default=0)

class Favourites(db.Model):

    user_id=db.Column(db.Integer,db.ForeignKey("user_info.user_id",ondelete='cascade'),primary_key=True)
    song_id=db.Column(db.Integer,db.ForeignKey("songs.song_id",ondelete='cascade'),primary_key=True)


class Playlists(db.Model):

    user_id=db.Column(db.Integer,db.ForeignKey("user_info.user_id"),primary_key=True)
    playlist_name=db.Column(db.String,primary_key=True)
    song_id=db.Column(db.Integer,db.ForeignKey("songs.song_id"),primary_key=True)


class AlbumFlags(db.Model):
    
    album_id=db.Column(db.Integer,db.ForeignKey('albums.album_name'),primary_key=True)
    user_id=db.Column(db.Integer,db.ForeignKey('user_info.user_id'),primary_key=True)


class Albums(db.Model):

    album_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    singer_id=db.Column(db.Integer,db.ForeignKey("user_info.user_id"))
    album_name=db.Column(db.String)
    flags=db.Column(db.Integer,default=0)
    song_id=db.Column(db.Integer,db.ForeignKey("songs.song_id"))
    genre=db.Column(db.String)

    flags=db.relationship("AlbumFlags",backref="album_data")


class AdminInfo(db.Model):

    admin_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    admin_username=db.Column(db.String(40),nullable=False)
    password=db.Column(db.String(256),nullable=False)
    counter=db.Column(db.Integer)