"""Initialize app."""

from flask import Flask


def init_app():
    """Construct the core app object."""
    app = Flask(__name__, template_folder="templates", static_folder="static")

    # Application Configuration
    app.config.from_object('config.Config')

    # Initialize Plugins
    from .extensions import db, login_manager, migrate
    
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)


    with app.app_context():
        from . import routes
        from . import auth
        
        # Register Blueprints
        app.register_blueprint(auth.auth_bp)

        # Create Database Models
        db.create_all()
        
        return app
