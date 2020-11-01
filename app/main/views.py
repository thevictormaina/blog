import datetime

from flask import redirect, render_template, request, url_for
from flask_login import current_user, login_required

from .. import db, photos
from ..models import Blogpost, Comment, Subscriber, User
from . import main

@main.route("/")
def index():
    """
    View function to return homepage
    """
    return render_template("homepage/index.html")