from flask import Flask
from .extensions.db import db
from .config import Config
from flask_migrate import Migrate


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Initialize DB
    db.init_app(app)
    
    migrate = Migrate(app, db)

    @app.route('/')
    def welcome_route():
        return "Welcome to the Flask Application!"

    # Register Blueprints (routes)
    from .routes.user_routes import user_bp
    
    app.register_blueprint(user_bp)

    # Register middleware (if global)
    from .middlewares.auth_middleware import register_middlewares
    register_middlewares(app)


    return app
