"""Routes for user authentication."""

from flask import Blueprint, redirect, render_template, flash, request, session, url_for
from flask_login import login_required, logout_user, current_user, login_user
from application.forms import LoginForm, SignupForm
from application.models import db, User, Role
from application.extensions import login_manager


# Blueprint Configuration
auth_bp = Blueprint(
    'auth_bp', __name__,
    template_folder='templates',
    static_folder='static'
)


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    
    form = LoginForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('auth_bp.login'))
        
        login_user(user, remember=form.remember_me.data)
        
        return redirect(url_for('home'))
    
    return render_template("auth/login.jinja2", title="Sign In", form=form)


@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    """
    User sign-up page.

    GET requests serve sign-up page.
    POST requests validate form & user creation.
    """
    
    form = SignupForm()
    roles = [(role.id, role.name) for role in Role.query.order_by('name')]
    form.role.choices = [(0, "Select Role"), *roles]
    
    if form.validate_on_submit() or request.method == 'POST':
        existing_user = User.query.filter_by(email=form.email.data).first()
        
        if existing_user is None:
            user = User(
                fname=form.fname.data,
                lname=form.lname.data,
                email=form.email.data,
                contact=form.contact.data,
                role_id=form.role.data
            )
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()  # Create new user
            login_user(user)  # Log in as newly created user
            
            return redirect(url_for('home'))
        
        flash('A user already exists with that email address.')
    
    return render_template(
        'auth/register.jinja2',
        title='Register Now',
        form=form,
    )


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

