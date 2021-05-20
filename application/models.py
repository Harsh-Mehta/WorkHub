"""Database models."""

from .extensions import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class Role(db.Model):
    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    users = db.relationship('User', backref=db.backref("role", lazy=True))


class User(UserMixin, db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(50), nullable=False, unique=False)
    lname = db.Column(db.String(50), nullable=False, unique=False)
    contact = db.Column(db.String(12), nullable=False, unique=True)
    email = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(200), primary_key=False, unique=False, nullable=False)
    
    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"), nullable=False)
    
    job_seekers = db.relationship('JobSeeker', backref=db.backref("user", lazy=True))
    recruiters = db.relationship('Recruiter', backref=db.backref("user", lazy=True))
    admins = db.relationship('Admin', backref=db.backref("user", lazy=True))
    banned_users = db.relationship('BannedUser', backref=db.backref("user", lazy=True))
    

    def set_password(self, password):
        """Create hashed password."""
        
        self.password = generate_password_hash(
            password,
            method='sha256'
        )

    def check_password(self, password):
        """Check hashed password."""
        
        return check_password_hash(self.password, password)

    def __repr__(self):
        return '<User {} {}>'.format(self.fname, self.lname)


class JobSeeker(db.Model):
    __tablename__ = "job_seekers"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    cv_uploaded = db.Column(db.Boolean, nullable=False, unique=False, default=False)
    ratings = db.Column(db.Float, nullable=False, unique=False, default=0)


class Recruiter(db.Model):
    __tablename__ = "recruiters"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    ratings = db.Column(db.Float, nullable=False, unique=False, default=0)


class Admin(db.Model):
    __tablename__ = "admin"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)


class BannedUsers(db.Model):
    __tablename__ = "banned_users"
    
    admin_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    reason = db.Column(db.String, unique=False, nullable=False)
