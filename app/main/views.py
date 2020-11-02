import datetime

from flask import redirect, render_template, request, url_for
from flask_login import current_user, login_required

from .. import db, photos
from ..models import Blogpost, Comment, Subscriber, User
from ..services import request_quote
from . import main


@main.route("/")
def index():
    """
    View function to return homepage
    """
    api_url = request_quote()

    blogposts = Blogpost.query.all()

    return render_template("index.html", quote = api_url, blogposts = blogposts)

@main.route("/<user_name>/subscribe", methods=["GET", "POST"])
def subscribe(user_name):
    """
    View function that displays form for reader to subscribe via email
    """
