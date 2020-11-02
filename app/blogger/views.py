from flask import flash, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user

from ..models import User, Subscriber, Blogpost
from ..services.email import mail_message
from . import blogger
# from .forms import NewBlogpost
from .. import db, simple

@blogger.route("/<user_name>", methods=["GET", "POST"])
def profile(user_name):
    """
    View function for displaying blogger's profile page

    Readers: can view blogger's profile
    Bloggers: can change profile picture. Also has create new post button
    """
    user = User.query.filter_by(user_name = user_name).first()

    title = f"Unload - {user_name}"
    return render_template("blogger/profile.html", user = user)

@blogger.route("/<user_name>/post/<blogpost_id>", methods=["GET", "POST"])
def blogpost(user_name, blogpost_id):
    """
    View function for displaying blogposts.

    Readers: can read post by blogger and leave comments
    Bloggers: can view post and delete comments
    """

    return render_template("blogger/blogpost.html")

@blogger.route("/new-post", methods=["GET", "POST"])
@login_required
def create_blogpost():
    """
    View function for displaying new blogpost form
    """

@blogger.route("/<user_name>/subscribers")
@login_required
def subscribers(user_name):
    """
    View function for displaying list of blogger's subscribers
    """