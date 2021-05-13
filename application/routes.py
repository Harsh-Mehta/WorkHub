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

@app.route("/jobDetail",methods=["GET", "POST"])
@login_required
def jobDetail():
    return render_template("pages/jobDetail.jinja2")

@app.route("/seekerNotification",methods=["GET", "POST"])
@login_required
def seekerNotification():
    return render_template("pages/seekerNotification.jinja2")

@app.route("/postJob",methods=["GET", "POST"])
@login_required
def recruiterPostJob():
    return render_template("pages/recruiter_post_job.jinja2")

@app.route("/postedJobs",methods=["GET", "POST"])
@login_required
def recruiterPostedJobs():
    return render_template("pages/recruiter_posted_jobs.jinja2")

@app.route("/applicants",methods=["GET", "POST"])
@login_required
def recruiterViewApplicants():
    return render_template("pages/recruiter_view_applicants.jinja2")
