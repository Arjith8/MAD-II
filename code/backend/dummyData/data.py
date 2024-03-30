import sqlite3, bcrypt
from datetime import datetime

# # Get the current date
# current_date = datetime.now().strftime('%Y-%m-%d')

# print(current_date)

conn=sqlite3.connect('../instance/projectDB.sqlite3')
cur=conn.cursor()


# ================================= FOR TABLE UserInfo ===================================

# user_data={
#     1: ['John', 'Doe', 'johndoe', 'password1', 'normal', 'johndoe@example.com'], 
#     2: ['Ryan', 'McCaffrey', 'Ryan McCaffrey', 'password2', 'creator', 'ryanmccaffrey@example.com'], 
#     3: ['Michael', 'Johnson', 'michaelj', 'password3', 'normal', 'michaelj@example.com'],
#     4: ['Emily', 'Brown', 'emilyb', 'password4', 'normal', 'emilyb@example.com'],
#     5: ['Quincas', 'Moreira', 'Quincas Moreira', 'password5', 'creator', 'quincasmoreira@example.com'], 
#     6: ['Sarah', 'Taylor', 'saraht', 'password6', 'normal', 'saraht@example.com'],
#     7: ['Aakash', 'Gandhi', 'Aakash Gandhi', 'password7', 'creator', 'aakashgandhi@example.com'], 
#     8: ['Linda', 'Martinez', 'TrackTribe', 'password8', 'creator', 'tracktribe@example.com'], 
#     9: ['Robert', 'White', 'robertw', 'password9', 'normal', 'robertw@example.com'],
#     10: ['Maria', 'Garcia', 'mariag', 'password10', 'normal', 'mariag@example.com'],
#     11: ['Temary', 'Blake', 'Temary Blake', 'password11', 'creator', 'temaryblake@example.com'],
#     12: ['Jennifer', 'Clark', 'jenniferc', 'password12', 'normal', 'jenniferc@example.com'],
#     13: ['Andrea', 'Dixit', 'Andrea Dixit', 'password13', 'creator', 'andreadixit@example.com'],
#     14: ['Susan', 'Thomas', 'susant', 'password14', 'normal', 'susant@example.com'],
#     15: ['Charles', 'Harris', 'charlesh', 'password15', 'normal', 'charlesh@example.com'],
#     16: ['Karen', 'Lewis', 'karenl', 'password16', 'normal', 'karenl@example.com'],
#     17: ['Richard', 'Jackson', 'richardj', 'password17', 'normal', 'richardj@example.com'],
#     18: ['Patricia', 'Brown', 'patriciab', 'password18', 'normal', 'patriciab@example.com'],
#     19: ['Daniel', 'Moore', 'danielm', 'password19', 'normal', 'danielm@example.com'],
#     20: ['Lisa', 'Lee', 'lisal', 'password20', 'normal', 'lisal@example.com']
# }


# for i in user_data:
    
#     current_date = datetime.now().strftime('%Y-%m-%d')
#     print(current_date)
#     sub_user_data=user_data[i]
#     passwd=sub_user_data[3].encode('utf-8')
#     encr=bcrypt.hashpw(passwd,bcrypt.gensalt())
#     stmt='insert into user_info (first_name,last_name,username,password,account_type,last_seen,sign_up_date,blacklisted,email) values (?,?,?,?,?,?,?,?,?)'
#     values=(sub_user_data[0],sub_user_data[1],sub_user_data[2],encr,sub_user_data[4],current_date,current_date,False,sub_user_data[-1])
#     print(values)
#     cur.execute(stmt,values)
#     conn.commit()


# ##================================= FOR TABLE Songs ===================================

# newsongs=[
#     ['Last To Know', 'Ryan McCaffrey', '15-01-2023', 0, 100000, 3.9],
#     ['Ticklish', 'Quincas Moreira', '25-11-2022', 0, 75000, 2.54], 
#     ['Shake It', 'Aakash Gandhi', '10-03-2023', 0, 125000, 5.0], 
#     ['AnaCaptainslogue', 'Ryan McCaffrey', '05-09-2022', 0, 82000, 2.94], 
#     ['Apolllo', 'TrackTribe', '20-12-2022', 0, 95000, 4.14], 
#     ['Silver Waves', 'TrackTribe', '05-02-2023', 0, 110000, 4.55], 
#     ['Arpy', 'TrackTribe', '15-10-2022', 0, 88000, 3.5], 
#     ['Final Girl', 'Temary Blake', '25-08-2022', 0, 93000, 3.91], 
#     ['Better Days', 'Quincas Moreira', '20-01-2023', 0, 76000, 2.81], 
#     ['Broken', 'Ryan McCaffrey', '10-12-2022', 0, 82000, 3.58], 
#     ['Care About You', 'Ryan McCaffrey', '05-04-2023', 0, 105000, 4.08], 
#     ['Crazy', 'Ryan McCaffrey', '30-11-2022', 0, 89000, 3.78], 
#     ['Time Slips By', 'Ryan McCaffrey', '15-03-2023', 0, 115000, 4.43], 
#     ['Raga Legacy', 'Andrea Dixit', '20-10-2022', 0, 74000, 3.08], 
#     ['Deck The Halls', 'Quincas Moreira', '01-12-2022', 0, 72000, 3.17], 
#     ['Dover', 'TrackTribe', '10-02-2023', 0, 72000, 3.1], 
#     ['First Of 3', 'Temary Blake', '15-09-2022', 0, 80000, 2.83], 
#     ['Forgiveness', 'Aakash Gandhi', '25-12-2022', 0, 95000, 3.64], 
#     ['Hey There', 'Andrea Dixit', '10-01-2023', 0, 112000, 4.6], 
#     ['Go!', 'Quincas Moreira', '15-11-2022', 0, 77000, 2.98], 
#     ['Joy To The World', 'Andrea Dixit', '20-03-2023', 0, 125000, 4.69], 
#     ["How's It Supposed to Feel (Clean)", 'Quincas Moreira', '05-02-2023', 0, 92000, 3.84], 
#     ['Keep It 98 Plus 2', 'Temary Blake', '15-01-2023', 0, 105000, 3.68], 
#     ['Life After Death', 'Temary Blake', '10-04-2023', 0, 90000, 3.78], 
#     ['Keys', 'Quincas Moreira', '01-12-2022', 0, 82000, 3.41], 
#     ['New Moon', 'Aakash Gandhi', '25-11-2022', 0, 95000, 3.62], 
#     ['Oh Christmas Tree', 'Andrea Dixit', '20-01-2023', 0, 88000, 3.35], 
#     ['Pila Pala Paradise', 'Aakash Gandhi', '10-02-2023', 0, 95000, 3.67], 
#     ['Playdate', 'Andrea Dixit', '05-09-2022', 0, 110000, 4.11], 
#     ['Ready or Not', 'TrackTribe', '15-03-2023', 0, 115000, 4.26], 
#     ['Santa Teresa', 'Andrea Dixit', '25-08-2022', 0, 86000, 3.56], 
#     ['Shadowing', 'Andrea Dixit', '15-10-2022', 0, 83000, 2.85], 
#     ['She No Dull Beat', 'Temary Blake', '20-12-2022', 0, 85000, 3.62], 
#     ['Take Me Down To The Fashion Show', 'TrackTribe', '30-11-2022', 0, 90000, 3.11], 
#     ["That's What It Takes", 'Quincas Moreira', '05-04-2023', 0, 95000, 3.35], 
#     ['Time Parade', 'Aakash Gandhi', '10-01-2023', 0, 102000, 3.84], 
#     ['Unstoppable', 'Aakash Gandhi', '01-09-2022', 0, 107000, 3.8]
# ]

# from mutagen.mp3 import MP3

# import random
# lis=['Pop','Jazz','Electronic','Instrumental']
# singer_dict={
#     'Ryan McCaffrey': 2,
#     'Quincas Moreira':5,
#     'Aakash Gandhi':7,
#     'TrackTribe':8,
#     'Temary Blake':11,
#     'Andrea Dixit':13
# }

# def dateConversion(date):
#     date=date.split('-')
#     date=date[::-1]
#     date="-".join(date)
#     return date


# for i in newsongs:
#     ch=random.choice(lis)

#     filename = f"../static/Tracks/{i[0]}.mp3"

#     mp3 = MP3(filename)
#     duration = mp3.info.length

#     formatted_duration = f"{duration:.2f}"

#     stmt='insert into songs(song_name,singer_id,genre,release_date,playback_count,count,rating_sum,duration) values(?,?,?,?,?,?,?,?)'
#     cur.execute(stmt,(i[0],singer_dict[i[1]],ch,dateConversion(i[2]),i[4],100,i[5]*100,duration))
#     conn.commit()


# ================================= FOR TABLE Albums ===================================


# albums = [
#     [2,"Ethereal Echoes","Pop"],
#     [5,"Timeless Reverie",'Pop'],
#     [7,"Neon Dreamscape",'Pop'],
#     [8,"Sonic Odyssey",'Jazz'],
#     [11,"Lost in Tranquility",'Electronic'],
#     [13,"Celestial Harmonies",'Instrumental']
# ]

# for i in albums:
#     stmt='insert into albums (singer_id,album_name,genre) values (?,?,?)'
#     cur.execute(stmt,(i[0],i[1],i[2]))
#     conn.commit()

# album_songs=[
#     [1,1], [1,10], [1,11], [1,12],   
#     [2,15], [2,22], [2,25], [2,35],   
#     [3,3], [3,36], [3,37], [3,28],
#     [4,5], [4,6], [4,30], [4,7],    
#     [5,8], [5,23], [5,24], [5,33],    
#     [6,19], [6,21], [6,29], [6,31],    
# ]

# for i in album_songs:
#     stmt = 'insert into album_songs(album_id,song_id) values (?,?)'
#     cur.execute(stmt,(i[0],i[1]))
#     conn.commit()



# for i in albums:
#     stmt='insert into albums (singer_id,album_name,song_id,genre) values (?,?,?,?)'
#     cur.execute(stmt,(i[0],i[1],i[2],dic[i[1]]))
#     conn.commit()
# temp=[]
# for i in albums:
#     if i[1] not in temp:
#         stmt='insert into album_flags (album_name,flags) values (?,?)'
#         cur.execute(stmt,(i[1],0))
#         conn.commit()
#         temp.append(i[1])

# ##================================= FOR TABLE AdminInfo ===================================

admin_data=[
    ['matthewm','password41'],
]


for i in admin_data:
    
    u=i[0].encode('utf-8')
    p=i[1].encode('utf-8')
    n=0
    u_encr=bcrypt.hashpw(u,bcrypt.gensalt())
    p_encr=bcrypt.hashpw(p,bcrypt.gensalt())
    stmt='insert into admin_info (admin_username,password,counter) values(?,?,?)'
    cur.execute(stmt,(u_encr,p_encr,0))
    conn.commit()

# ##================================= FOR TABLE Favourites ===================================

# from datetime import datetime
# for i in range(1,6):
    
#     t = datetime.now().strftime('%Y-%m-%d')
#     stmt="insert into favourites (user_id,song_id,favorited_on) values (?,?,?)"
#     cur.execute(stmt,(1,i,t))
#     conn.commit()

# ====================================== PLAYLISTS ==========================================

# import random
# import shutil

# playlist_data=[
#     ["Johns's Playlist",1],
#     ["Quincas' Playlist",5],
#     ["Aakash's Playlist",7],
#     ["TrackTribe's Playlist",8],
#     ["Temary's Playlist",11],
#     ["Andrea's Playlist",13]
# ]

# playlist_songs=[
#     [1,1],[1,10],[1,11],[1,12],
#     [2,15],[2,22],[2,25],[2,35],
#     [3,3],[3,36],[3,37],[3,28],
#     [4,5],[4,6],[4,30],[4,7],
#     [5,8],[5,23],[5,24],[5,33],
#     [6,19],[6,21],[6,29],[6,31]
# ]

# random_number = random.randint(1,37)


# counter = 0

# for i in playlist_data:
#     counter +=1
#     image = f"C:/New folder (2)/MAD-II/code/frontend/public/song/{random_number}.jpg"
#     to = f"C:/New folder (2)/MAD-II/code/frontend/public/playlist/{counter}.jpg"

#     stmt="insert into playlists (user_id,playlist_name) values (?,?)"
#     cur.execute(stmt,(i[1],i[0]))
#     conn.commit()
#     shutil.copy(image,to)

# for i in playlist_songs:
#     stmt="insert into playlist_songs (playlist_id,song_id) values (?,?)"
#     cur.execute(stmt,(i[0],i[1]))
#     conn.commit()