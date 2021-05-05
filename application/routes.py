from flask import render_template, redirect, url_for
from flask import current_app as app
from flask_login import logout_user, login_required



@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def home():
    return "This is homepage."


@app.route("/logout")
@login_required
def logout():
    """User log-out logic."""
    logout_user()
    return redirect(url_for('auth_bp.login'))
