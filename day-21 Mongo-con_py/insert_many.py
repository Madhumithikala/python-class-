#import pymongo

from pymongo import MongoClient
client=None
try:
    client=MongoClient('mongodb://localhost:27017/')
    db=client['db2']
    user_col=db['users']
    users=[{'eid':1,'ename':'madhu','email':'madhu@gmail.com','gender':'Male'},
    {'eid':2,'ename':'balaji','email':'balaji@gmail.com','gender':'Male'},
    {'eid':3,'ename':'gnana','email':'gnana@gmail.com','gender':'Male'},
    {'eid':4,'ename':'srinithi','email':'srinithi@gmail.com','gender':'Female'},
    {'eid':5,'ename':'madhu','email':'madhu@gmail.com','gender':'Female'}
    ];
    user_col.insert_many(users)
    print("inserted documents successfully")
except:
    print("unable  to print")
finally:
    client.close()