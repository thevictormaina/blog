from flask import render_template
from flask_mail import Message

from ..app import mail

def mail_message(subject, template, to, **kwargs):
    """
    Function to send welcome email to new User
    """
    sender_email = "moringacoreprojects@gmail.com"

    email = Message(subject, sender=sender_email, recipients=[to])
    email.body = render_template(template + ".txt", **kwargs)
    email.html = render_template(template + ".html", **kwargs)

    mail.send(email)