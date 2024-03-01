import sqlite3, bcrypt
from datetime import datetime

# # Get the current date
# current_date = datetime.now().strftime('%Y-%m-%d')

# print(current_date)

conn=sqlite3.connect('../instance/projectDB.sqlite3')
cur=conn.cursor()


# ================================= FOR TABLE UserInfo ===================================

# user_data={
# 	1: ['John', 'Doe', 'johndoe', 'password1', 'normal'], 
# 	2: ['Ryan', 'McCaffrey', 'Ryan McCaffrey', 'password2', 'creator'], 
# 	3: ['Michael', 'Johnson', 'michaelj', 'password3', 'normal'],
# 	4: ['Emily', 'Brown', 'emilyb', 'password4', 'normal'],
# 	5: ['Quincas', 'Moreira', 'Quincas Moreira', 'password5', 'creator'], 
# 	6: ['Sarah', 'Taylor', 'saraht', 'password6', 'normal'],
# 	7: ['Aakash', 'Gandhi', 'Aakash Gandhi', 'password7', 'creator'], 
# 	8: ['Linda', 'Martinez', 'TrackTribe', 'password8', 'creator'], 
# 	9: ['Robert', 'White', 'robertw', 'password9', 'normal'],
# 	10: ['Maria', 'Garcia', 'mariag', 'password10', 'normal'],
# 	11: ['Temary', 'Blake', 'Temary Blake', 'password11', 'creator'],
# 	12: ['Jennifer', 'Clark', 'jenniferc', 'password12', 'normal'],
# 	13: ['Andrea', 'Dixit', 'Andrea Dixit', 'password13', 'creator'],
# 	14: ['Susan', 'Thomas', 'susant', 'password14', 'normal'],
# 	15: ['Charles', 'Harris', 'charlesh', 'password15', 'normal'],
# 	16: ['Karen', 'Lewis', 'karenl', 'password16', 'normal'],
# 	17: ['Richard', 'Jackson', 'richardj', 'password17', 'normal'],
# 	18: ['Patricia', 'Brown', 'patriciab', 'password18', 'normal'],
# 	19: ['Daniel', 'Moore', 'danielm', 'password19', 'normal'],
# 	20: ['Lisa', 'Lee', 'lisal', 'password20', 'normal']
# }


# for i in user_data:
    
#     current_date = datetime.now().strftime('%Y-%m-%d')
#     print(current_date)
#     sub_user_data=user_data[i]
#     passwd=sub_user_data[3].encode('utf-8')
#     encr=bcrypt.hashpw(passwd,bcrypt.gensalt())
#     stmt='insert into user_info (first_name,last_name,username,password,account_type,last_seen,sign_up_date,blacklisted) values (?,?,?,?,?,?,?,?)'
#     values=(sub_user_data[0],sub_user_data[1],sub_user_data[2],encr,sub_user_data[4],current_date,current_date,False)
#     cur.execute(stmt,values)
#     conn.commit()


# # ##================================= FOR TABLE Songs ===================================

newsongs=[
    ['Last To Know', 'Ryan McCaffrey', '15-01-2023', 0, 100000, 3.9],
    ['Ticklish', 'Quincas Moreira', '25-11-2022', 0, 75000, 2.54], 
    ['Shake It', 'Aakash Gandhi', '10-03-2023', 0, 125000, 5.0], 
    ['AnaCaptainslogue', 'Ryan McCaffrey', '05-09-2022', 0, 82000, 2.94], 
    ['Apolllo', 'TrackTribe', '20-12-2022', 0, 95000, 4.14], 
    ['Silver Waves', 'TrackTribe', '05-02-2023', 0, 110000, 4.55], 
    ['Arpy', 'TrackTribe', '15-10-2022', 0, 88000, 3.5], 
    ['Final Girl', 'Temary Blake', '25-08-2022', 0, 93000, 3.91], 
    ['Better Days', 'Quincas Moreira', '20-01-2023', 0, 76000, 2.81], 
    ['Broken', 'Ryan McCaffrey', '10-12-2022', 0, 82000, 3.58], 
    ['Care About You', 'Ryan McCaffrey', '05-04-2023', 0, 105000, 4.08], 
    ['Crazy', 'Ryan McCaffrey', '30-11-2022', 0, 89000, 3.78], 
    ['Time Slips By', 'Ryan McCaffrey', '15-03-2023', 0, 115000, 4.43], 
    ['Raga Legacy', 'Andrea Dixit', '20-10-2022', 0, 74000, 3.08], 
    ['Deck The Halls', 'Quincas Moreira', '01-12-2022', 0, 72000, 3.17], 
    ['Dover', 'TrackTribe', '10-02-2023', 0, 72000, 3.1], 
    ['First Of 3', 'Temary Blake', '15-09-2022', 0, 80000, 2.83], 
    ['Forgiveness', 'Aakash Gandhi', '25-12-2022', 0, 95000, 3.64], 
    ['Hey There', 'Andrea Dixit', '10-01-2023', 0, 112000, 4.6], 
    ['Go!', 'Quincas Moreira', '15-11-2022', 0, 77000, 2.98], 
    ['Joy To The World', 'Andrea Dixit', '20-03-2023', 0, 125000, 4.69], 
    ["How's It Supposed to Feel (Clean)", 'Quincas Moreira', '05-02-2023', 0, 92000, 3.84], 
    ['Keep It 98 Plus 2', 'Temary Blake', '15-01-2023', 0, 105000, 3.68], 
    ['Life After Death', 'Temary Blake', '10-04-2023', 0, 90000, 3.78], 
    ['Keys', 'Quincas Moreira', '01-12-2022', 0, 82000, 3.41], 
    ['New Moon', 'Aakash Gandhi', '25-11-2022', 0, 95000, 3.62], 
    ['Oh Christmas Tree', 'Andrea Dixit', '20-01-2023', 0, 88000, 3.35], 
    ['Pila Pala Paradise', 'Aakash Gandhi', '10-02-2023', 0, 95000, 3.67], 
    ['Playdate', 'Andrea Dixit', '05-09-2022', 0, 110000, 4.11], 
    ['Ready or Not', 'TrackTribe', '15-03-2023', 0, 115000, 4.26], 
    ['Santa Teresa', 'Andrea Dixit', '25-08-2022', 0, 86000, 3.56], 
    ['Shadowing', 'Andrea Dixit', '15-10-2022', 0, 83000, 2.85], 
    ['She No Dull Beat', 'Temary Blake', '20-12-2022', 0, 85000, 3.62], 
    ['Take Me Down To The Fashion Show', 'TrackTribe', '30-11-2022', 0, 90000, 3.11], 
    ["That's What It Takes", 'Quincas Moreira', '05-04-2023', 0, 95000, 3.35], 
    ['Time Parade', 'Aakash Gandhi', '10-01-2023', 0, 102000, 3.84], 
    ['Unstoppable', 'Aakash Gandhi', '01-09-2022', 0, 107000, 3.8]
]

from mutagen.mp3 import MP3

import random
lis=['Pop','Jazz','Electronic','Instrumental']
singer_dict={
    'Ryan McCaffrey': 2,
    'Quincas Moreira':5,
    'Aakash Gandhi':7,
    'TrackTribe':8,
    'Temary Blake':11,
    'Andrea Dixit':13
}
for i in newsongs:
    ch=random.choice(lis)
    duration=MP3(f'../../static/Tracks/{i[0]}.mp3').info.length
    stmt='insert into songs(song_name,singer_id,genre,release_date,flags,playback_count,count,rating_sum,duration) values(?,?,?,?,?,?,?,?,?)'
    cur.execute(stmt,(i[0],singer_dict[i[1]],ch,i[2],i[3],i[4],100,i[5]*100,duration))
    conn.commit()

# ##================================= FOR TABLE Albums ===================================


# albums=[
    
#     [2,"Ethereal Echoes",1],
#     [2,"Ethereal Echoes",10],
#     [2,"Ethereal Echoes",11],
#     [2,"Ethereal Echoes",12],
    
#     [5,"Timeless Reverie",15],
#     [5,"Timeless Reverie",22],
#     [5,"Timeless Reverie",25],
#     [5,"Timeless Reverie",35],
    
#     [7,"Neon Dreamscape",3],
#     [7,"Neon Dreamscape",36],
#     [7,"Neon Dreamscape",37],
#     [7,"Neon Dreamscape",28],
    
#     [8,"Sonic Odyssey",5],
#     [8,"Sonic Odyssey",6],
#     [8,"Sonic Odyssey",30],
#     [8,"Sonic Odyssey",7],
    
#     [11,"Lost in Tranquility",8],
#     [11,"Lost in Tranquility",23],
#     [11,"Lost in Tranquility",24],
#     [11,"Lost in Tranquility",33],
    
#     [13,"Celestial Harmonies",19],
#     [13,"Celestial Harmonies",21],
#     [13,"Celestial Harmonies",29],
#     [13,"Celestial Harmonies",31],
    
# ]

# for i in albums:
#     stmt='insert into albums (singer_id,album_name,song_id) values (?,?,?)'
#     cur.execute(stmt,(i[0],i[1],i[2]))
#     conn.commit()
# temp=[]
# for i in albums:
#     if i[1] not in temp:
#         stmt='insert into album_flags (album_name,flags) values (?,?)'
#         cur.execute(stmt,(i[1],0))
#         conn.commit()
#         temp.append(i[1])

# ##================================= FOR TABLE AdminInfo ===================================

# admin_data=[
#     ['matthewm','password41'],
#     ['jessicaj','password42'],
#     ['christopherb','password43']
# ]


# for i in admin_data:
    
#     u=i[0].encode('utf-8')
#     p=i[1].encode('utf-8')
#     n=0
#     u_encr=bcrypt.hashpw(u,bcrypt.gensalt())
#     p_encr=bcrypt.hashpw(p,bcrypt.gensalt())
#     stmt='insert into admin_info (admin_username,password,counter) values(?,?,?)'
#     cur.execute(stmt,(u_encr,p_encr,0))
#     conn.commit()

# ##================================= FOR TABLE Favourites ===================================


# for i in range(1,6):
    
#     stmt="insert into favourites (user_id,song_id) values (?,?)"
#     cur.execute(stmt,(1,i))
#     conn.commit()


#================================= FOR TABLE UserInfo ===================================





# ===============================DATED===========================

# # for i in questions_data:
# #     date=i[2]
# #     date=date.split('-')
# #     new_date=date[2]+'-'+date[1]+'-'+date[0]
# #     i[2]=new_date

# newsongs=[
#     ['Last To Know', 'Ryan McCaffrey', '15-01-2023', 0, 100000],
#     ['Ticklish', 'Quincas Moreira', '25-11-2022', 0, 75000], 
#     ['Shake It', 'Aakash Gandhi', '10-03-2023', 0, 125000], 
#     ['AnaCaptainslogue', 'Ryan McCaffrey', '05-09-2022', 0, 82000], 
#     ['Apolllo', 'TrackTribe', '20-12-2022', 0, 95000], 
#     ['Silver Waves', 'TrackTribe', '05-02-2023', 0, 110000], 
#     ['Arpy', 'TrackTribe', '15-10-2022', 0, 88000], 
#     ['Final Girl', 'Temary Blake', '25-08-2022', 0, 93000], 
#     ['Better Days', 'Quincas Moreira', '20-01-2023', 0, 76000],
#     ['Broken', 'Ryan McCaffrey', '10-12-2022', 0, 82000],
#     ['Care About You', 'Ryan McCaffrey', '05-04-2023', 0, 105000], 
#     ['Crazy', 'Ryan McCaffrey', '30-11-2022', 0, 89000], 
#     ['Time Slips By', 'Ryan McCaffrey', '15-03-2023', 0, 115000], 
#     ['Raga Legacy', 'Andrea Dixit', '20-10-2022', 0, 74000], 
#     ['Deck The Halls', 'Quincas Moreira', '01-12-2022', 0, 72000], 
#     ['Dover', 'TrackTribe', '10-02-2023', 0, 72000], 
#     ['First Of 3', 'Temary Blake', '15-09-2022', 0, 80000], 
#     ['Forgiveness', 'Aakash Gandhi', '25-12-2022', 0, 95000], 
#     ['Hey There', 'Andrea Dixit', '10-01-2023', 0, 112000], 
#     ['Go!', 'Quincas Moreira', '15-11-2022', 0, 77000],
#     ["Joy To The World", "Andrea Dixit", "20-03-2023", 0, 125000],
#     ["How's It Supposed to Feel (Clean)", "Quincas Moreira", "05-02-2023", 0, 92000],
#     ["Keep It 98 Plus 2", "Temary Blake", "15-01-2023", 0, 105000],
#     ["Life After Death", "Temary Blake", "10-04-2023", 0, 90000],
#     ["Keys", "Quincas Moreira", "01-12-2022", 0, 82000],
#     ["New Moon", "Aakash Gandhi", "25-11-2022", 0, 95000],
#     ["Oh Christmas Tree", "Andrea Dixit", "20-01-2023", 0, 88000],
#     ["Pila Pala Paradise", "Aakash Gandhi", "10-02-2023", 0, 95000],
#     ["Playdate", "Andrea Dixit", "05-09-2022", 0, 110000],
#     ["Ready or Not", "TrackTribe", "15-03-2023", 0, 115000],
#     ["Santa Teresa", "Andrea Dixit", "25-08-2022", 0, 86000],
#     ["Shadowing", "Andrea Dixit", "15-10-2022", 0, 83000],
#     ["She No Dull Beat", "Temary Blake", "20-12-2022", 0, 85000],
#     ["Take Me Down To The Fashion Show", "TrackTribe", "30-11-2022", 0, 90000],
#     ["That's What It Takes", "Quincas Moreira", "05-04-2023", 0, 95000],
#     ["Time Parade", "Aakash Gandhi", "10-01-2023", 0, 102000],
#     ["Unstoppable", "Aakash Gandhi", "01-09-2022", 0, 107000],
# ]

# import random

# for song in newsongs:
#     views = song[4]
#     rating = min(5.0, (views / 30000) + random.uniform(0, 1))
#     rating=float("{:.2f}".format(rating))
#     song.append(rating)
# print(newsongs)