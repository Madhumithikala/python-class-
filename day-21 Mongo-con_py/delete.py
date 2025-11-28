import pymongo
from pymongo import MongoClient
client=None
try:
    client=MongoClient('mongodb://localhost:27017/')
    db=client['db2']
    user_col=db['users']
    user_col.delete_one({"eid":1})
except mysql.connecter.Error as err:
    print(err)
finally:
    client.close()

