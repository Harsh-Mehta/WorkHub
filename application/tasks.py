import json

from flask import current_app
from flask_mail import Mail, Message

from application import celery
from application.extensions import mail


@celery.task(name="application.tasks.send_email")
def send_email(email_data):
    app = current_app._get_current_object()
    msg = Message(subject=email_data['subject'],
                  sender=email_data['from'],
                  recipients=[email_data['to']],
                  body=email_data['body'])

    with app.app_context():
        mail.send(msg)
