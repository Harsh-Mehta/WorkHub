from flask import render_template
from flask import current_app as app



@app.route("/", methods=["GET", "POST"])
def home():
    return "This is homepage."
