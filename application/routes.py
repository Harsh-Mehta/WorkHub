from flask import render_template, redirect, url_for
from flask import current_app as app
from flask_login import logout_user, login_required



@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
@login_required
def home():
    return render_template("pages/home.jinja2")


@app.route("/logout")
@login_required
def logout():
    """User log-out logic."""
    logout_user()
    return redirect(url_for('auth_bp.login'))


@app.route("/seekerProfile", methods=["GET", "POST"])
@login_required
def seekerProfile():
   return render_template("pages/seekerProfile.jinja2")

@app.route("/seekerStats", methods=["GET", "POST"])
@login_required
def seekerStats():
   return render_template("pages/seekerStats.jinja2")