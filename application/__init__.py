"""Initialize app."""

from flask import Flask
from celery import Celery
from flask_config import FlaskConfig
import celery_config
from application.celery_utils import init_celery
from application.extensions import db, login_manager, migrate, session, mail


# Instantiating Celery app
celery = Celery(__name__, broker=FlaskConfig.CELERY_BROKER_URL)


def create_roles(db):
    from application.models import Role

    roles = ["Admin", "Job Seeker", "Recruiter"]
    
    for role in roles:
        existing_role = Role.query.filter_by(name=role).first()
        
        if existing_role is None:
            role_obj = Role(name=role)
            db.session.add(role_obj)
            db.session.commit()


def create_job_statuses(db):
    from application.models import JobStatus

    statuses = list(sorted(["Approved", "Completed", "Waiting", "Rejected", "Hired", "Open"]))
    
    for status in statuses:
        existing_status = JobStatus.query.filter_by(name=status).first()
        
        if existing_status is None:
            status_obj = JobStatus(name=status)
            db.session.add(status_obj)
            db.session.commit()


def init_app():
    """Construct the core app object."""
    app = Flask(__name__, template_folder="templates", static_folder="static")
    app.config.from_object(FlaskConfig)

    """Initialize Plugins."""
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    session.init_app(app)
    mail.init_app(app)

    init_celery(celery, app)

    with app.app_context():
        from application import routes
        from application import auth
    
        # Register Blueprints
        app.register_blueprint(auth.auth_bp)

        # Create Database Models
        db.create_all()
        
        # Initial seed for user roles
        create_roles(db)
        create_job_statuses(db)
        
        return app
