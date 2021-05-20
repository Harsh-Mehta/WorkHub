"""Initialize app."""

from flask import Flask


def create_roles(db):
    from .models import Role

    roles = ["Admin", "Job Seeker", "Recruiter"]
    
    for role in roles:
        existing_role = Role.query.filter_by(name=role).first()
        if existing_role is None:
            role_obj = Role(name=role)
            db.session.add(role_obj)
            db.session.commit()


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
        
        # Initial seed for user roles
        create_roles(db)
        
        return app
