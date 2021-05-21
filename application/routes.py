from flask import render_template, redirect, url_for
from flask import current_app as app
from flask_login import logout_user, login_required
from application.tasks import send_email


@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
@login_required
def home():
    return render_template("pages/home.jinja2")


@app.route("/sendemail", methods=["GET", "POST"])
@login_required
def email_page():
    email_data = {
        'subject': 'Hello from the other side!',
        'from': "workhub-96b1de@inbox.mailtrap.io",
        'to': "workhub-96b1de@inbox.mailtrap.io",
        'body': 'Good job Harsh! Mail feature finally works.'
    }

    send_email.delay(email_data)
    return "Message sent!"

    # return redirect(url_for('index'))

@app.route("/logout")
@login_required
def logout():
    """User log-out logic."""
    logout_user()
    return redirect(url_for('auth_bp.login'))

@app.route("/search")
@login_required
def search():
    return render_template("pages/search.jinja2")

@app.route("/jobs")
@login_required
def jobs():
    return render_template("pages/jobs.jinja2")

@app.route("/messages")
@login_required
def messages():
    return render_template("pages/messages.jinja2")

