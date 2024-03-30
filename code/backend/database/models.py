from flask_sqlalchemy import SQLAlchemy

db=SQLAlchemy()

class UserInfo(db.Model):

    user_id=db.Column(db.Integer,autoincrement=True,primary_key=True,nullable=False)
    first_name=db.Column(db.String(40),nullable=False)
    last_name=db.Column(db.String(40),nullable=False)
    username=db.Column(db.String(40),nullable=False,unique=True)
    password=db.Column(db.String(256),nullable=False)
    email = db.Column(db.String,nullable=False)
    account_type=db.Column(db.String(10),nullable=False,default='normal')
    last_seen=db.Column(db.String,nullable=False)
    sign_up_date=db.Column(db.String,nullable=False)
    blacklisted=db.Column(db.Boolean,default=False)

class Songs(db.Model):

    song_id=db.Column(db.Integer,nullable=False,autoincrement=True,primary_key=True)
    singer_id=db.Column(db.Integer,db.ForeignKey("user_info.user_id",ondelete="cascade"),nullable=False)
    song_name=db.Column(db.String,nullable=False,unique=True)
    genre=db.Column(db.String,nullable=False)
    release_date=db.Column(db.String,nullable=False)
    playback_count=db.Column(db.Integer,default=0)
    count=db.Column(db.Integer,default=0)
    rating_sum=db.Column(db.Integer, default=0)
    duration=db.Column(db.Integer)

    creator_data = db.relationship("UserInfo",backref="songs")

class SongFlags(db.Model):
    song_id = db.Column(db.Integer,db.ForeignKey('songs.song_id'),primary_key=True)
    user_id = db.Column(db.Integer,db.ForeignKey('user_info.user_id'),primary_key=True)

    song_data=db.relationship("Songs",backref="song_flags")
    user_data=db.relationship("UserInfo",backref="flagged_songs")

class Lyrics(db.Model):
    
    lyrics_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    creator_id=db.Column(db.Integer,db.ForeignKey("user_info.user_id",ondelete="cascade"))
    lyrics_name=db.Column(db.String,nullable=False)
    release_date=db.Column(db.String,nullable=False)
    rating_sum=db.Column(db.Integer,default=0)
    count=db.Column(db.Integer,default=0)

    creator_data = db.relationship("UserInfo",backref="lyrics")



class Favourites(db.Model):

    user_id=db.Column(db.Integer,db.ForeignKey("user_info.user_id",ondelete='cascade'),primary_key=True)
    song_id=db.Column(db.Integer,db.ForeignKey("songs.song_id",ondelete='cascade'),primary_key=True)
    favorited_on = db.Column(db.String)

    user_data = db.relationship("UserInfo",backref="favourites")
    song_data=db.relationship("Songs",backref="fav_by")



class PlaylistSongs(db.Model):

    playlist_id = db.Column(db.Integer,db.ForeignKey("playlists.playlist_id"), primary_key=True)
    song_id=db.Column(db.Integer,db.ForeignKey("songs.song_id",ondelete='cascade'),primary_key=True)
    

    playlist_data = db.relationship("Playlists",backref = "playlist_songs_id")
    song_data = db.relationship("Songs",backref = "playlist_id")


class Playlists(db.Model):

    playlist_id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    user_id=db.Column(db.Integer,db.ForeignKey("user_info.user_id",ondelete='cascade'))
    playlist_name=db.Column(db.String)

    user_data = db.relationship("UserInfo",backref="playlist_data")


class AlbumFlags(db.Model):

    album_id = db.Column(db.String,db.ForeignKey('albums.album_id'),primary_key=True)
    user_id = db.Column(db.String,db.ForeignKey('user_info.user_id'),primary_key=True)

    album_data=db.relationship("Albums",backref="flags")
    user_data=db.relationship("UserInfo",backref="flagged_albums")


class AlbumSongs(db.Model):
    album_id = db.Column(db.Integer,db.ForeignKey("albums.album_id"),primary_key=True)
    song_id=db.Column(db.Integer,db.ForeignKey("songs.song_id"),primary_key=True)

    album_data = db.relationship('Albums',backref = "songs")
    song_data = db.relationship("Songs",backref="albums")



class Albums(db.Model):

    album_id = db.Column(db.Integer,primary_key = True, autoincrement = True)
    singer_id=db.Column(db.Integer,db.ForeignKey("user_info.user_id"))
    album_name=db.Column(db.String)
    genre=db.Column(db.String)

    creator_info=db.relationship("UserInfo",backref="albums")



class AdminInfo(db.Model):

    admin_id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    admin_username=db.Column(db.String(40),nullable=False,unique=True)
    password=db.Column(db.String(256),nullable=False)
    counter=db.Column(db.Integer)