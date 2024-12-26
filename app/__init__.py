from flask import Flask
from flask_pymongo import PyMongo

mongo = PyMongo()

def create_app():
    app = Flask(__name__)
    app.config.from_object('app.config.Config')
    mongo.init_app(app)

    # Register Blueprints
    from app.routes.user_routes import user_bp
    app.register_blueprint(user_bp, url_prefix='/users')

    return app
