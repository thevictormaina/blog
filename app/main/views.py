import datetime

from flask import redirect, render_template, request, url_for
from flask_login import current_user, login_required

from .. import db, photos
from ..models import Blogpost, Comment, Subscriber, User
from . import main
from ..services import request_quote


@main.route("/")
def index():
    """
    View function to return homepage
    """
    api_url = request_quote()
    return render_template("index.html", quote = api_url)

@main.route("/<user_name>/subscribe", methods=["GET", "POST"])
def subscribe(user_name):
    """
    View function that displays form for reader to subscribe via email
    """
