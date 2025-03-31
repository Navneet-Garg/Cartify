from flask import Flask
from flask_cors import CORS
from app.routes import (
    anomaly_routes,
    chatbot_routes,
    login_routes,
    recommendation_routes,
    search_routes
)
from app.utils.db import init_db
from app.config.settings import config

def create_app():
    app = Flask(__name__)
    CORS(app)

    # Load configuration
    app.config['MONGO_URI'] = config.MONGO_URI
    app.config['SECRET_KEY'] = config.SECRET_KEY
    app.config['DEBUG'] = config.DEBUG

    # Initialize database
    init_db(app)

    # Register blueprints with original endpoints
    app.register_blueprint(anomaly_routes.bp)
    app.register_blueprint(chatbot_routes.bp)
    app.register_blueprint(login_routes.bp)
    app.register_blueprint(recommendation_routes.bp)
    app.register_blueprint(search_routes.bp)


    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000) 