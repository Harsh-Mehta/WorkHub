"""Database models."""

from .extensions import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class Role(db.Model):
    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)


class User(UserMixin, db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    fname = db.Column(db.String(50), nullable=False, unique=False)
    lname = db.Column(db.String(50), nullable=False, unique=False)
    contact = db.Column(db.String(12), nullable=False, unique=True)
    email = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(200), primary_key=False, unique=False, nullable=False)
    created_on = db.Column(db.DateTime, index=False, unique=False, nullable=True)
    last_login = db.Column(db.DateTime, index=False, unique=False, nullable=True)

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
        return '<User {}>'.format(self.username)
