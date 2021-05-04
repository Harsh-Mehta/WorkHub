"""Routes for user authentication."""

from flask import Blueprint, render_template, redirect, url_for, flash
from .forms import LoginForm
from .models import User
from .extensions import login_manager
from flask_login import current_user, login_user
from flask.helpers import flash


# Blueprint Configuration
auth_bp = Blueprint(
    'auth_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    
    form = LoginForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('auth_bp.login'))
        
        login_user(user, remember=form.remember_me.data)
        
        return redirect(url_for('index'))
    
    return render_template("auth/login.jinja2", title="Login", form=form)


# @auth_bp.route('/signup', methods=['GET', 'POST'])
# def signup():
#     # Signup logic goes here
#     pass

@login_manager.user_loader
def load_user(user_id):
    """Check if user is logged-in on every page load."""
    
    if user_id is not None:
        return User.query.get(user_id)
    return None


@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    
    flash('You must be logged in to view that page.')
    return redirect(url_for('auth_bp.login'))

