from flask_pymongo import PyMongo
from app.config.settings import config

mongo = PyMongo()

def init_db(app):
    """Initialize MongoDB connection"""
    app.config['MONGO_URI'] = config.MONGO_URI
    mongo.init_app(app)
    return mongo 