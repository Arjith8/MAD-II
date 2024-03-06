import os

path='./Image/'
files=os.listdir(path)
path = os.path.abspath(path)
c=0
for i in files:
    print(i)
    c+=1
    os.rename(path+'/'+i,path+'/'+str(c)+'.jpg')
print(os.listdir(path))
