from flask_pymongo import PyMongo
from app.config.settings import MONGO_URI

mongo = PyMongo()

def init_db(app):
    mongo.init_app(app, uri=MONGO_URI)
    return mongo 