from flask_pymongo import PyMongo
import server as s

s.app.config['MONGO_DBNAME'] = 'conntect_to_mongo'
s.app.config['MONGO_URI'] = 'mongodb://<db_name>:<db_password>@ds261429.mlab.com:61429/conntect_to_mongo'
mongo = PyMongo(s.app)
