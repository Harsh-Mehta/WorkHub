from flask import render_template, redirect, url_for
from flask import current_app as app
from flask_login import logout_user, login_required
from application.tasks import send_email
from application.models import Job



@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
@login_required
def home():
    jobs = Job.query.all()
    return render_template("pages/home.jinja2", jobs=jobs)


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
