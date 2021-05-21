from flask import render_template, redirect, url_for, session, request
from flask import current_app as app
from flask_login import logout_user, login_required
from application.tasks import send_email
from application.models import Job, User, AppliedJob, JobStatus, JobSeeker
from application.forms import JobApplicationForm
from application.extensions import db



@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
@login_required
def home():
    jobs = Job.query.all()
    return render_template("pages/home.jinja2", jobs=jobs, session=session)


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


@app.route("/apply_job/<job_id>", methods=["GET", "POST"])
@login_required
def apply_job(job_id):
    form = JobApplicationForm()

    if not form.validate_on_submit() and request.method != 'POST':
        user = User.query.filter_by(id=session.get("_user_id")).first()
        return render_template("pages/job_apply.jinja2", current_user=user, job_id=job_id)

    job_exists = AppliedJob.query.filter_by(job_id=job_id).first()
    open_status = JobStatus.query.filter_by(name="Open").first()
    waiting_status = JobStatus.query.filter_by(name="Waiting").first()
    job_seeker = JobSeeker.query.filter_by(user_id=session.get("_user_id")).first()

    if job_exists is None or job_exists.status_id != open_status.id:
        applied_job = AppliedJob(job_id=int(job_id), seeker_id=job_seeker.id, status_id=waiting_status.id)  # Applied
        db.session.add(applied_job)
        db.session.commit()
        
        return redirect(url_for("home"))


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
