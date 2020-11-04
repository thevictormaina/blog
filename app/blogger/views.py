from flask import flash, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user, current_user
import markdown2

from .forms import NewBlogpost, CommentForm
from .. import db, simple, photos
from ..models import Blogpost, Comment, Subscriber, User
from ..services.email import mail_message
from . import blogger


@blogger.route("/<user_name>", methods=["GET", "POST"])
@login_required
def profile(user_name):
    """
    View function for displaying blogger's profile page

    Readers: can view blogger's profile
    Bloggers: can change profile picture. Also has create new post button
    """
    blogposts = Blogpost.query.filter_by(user_id = current_user.id).all()
    user = User.query.filter_by(user_name = user_name).first()

    title = f"Unload - {user_name}"
    return render_template("blogger/profile.html", user = user, blogposts = blogposts)

@blogger.route('/blogpost/<blogpost_id>', methods=["GET", "POST"])
def blogpost(blogpost_id):
    """
    View function for displaying blogposts.

    Readers: can read post by blogger and leave comments
    Bloggers: can view post and delete comments
    """
    comment_form = CommentForm()

    if comment_form.validate_on_submit():
        comment = Comment(full_name = comment_form.name.data, email = comment_form.email.data, comment = comment_form.comment.data, blogpost_id = blogpost_id)

        db.session.add(comment)
        db.session.commit()

    user = request.args.get("user_name")
    blogpost = Blogpost.query.filter_by(id = blogpost_id).first()

    comments = []
    for comment in Comment.query.filter_by(blogpost_id = blogpost_id).all():
        if comment.comment != "None":
            comments.append(comment)
            print("\nCOMMENT: ", comment.comment)
        else:
            pass

    body_format = markdown2.markdown(blogpost.body, extras = ["code-friendly", "fenced-code-blocks"])

    title = f"Unload - {blogpost.title}"

    return render_template("blogger/blog_post.html", user = user, blogpost = blogpost, body_format = body_format, title = title, comment_form = comment_form, comments = comments)

@blogger.route("/new-post", methods=["GET", "POST"])
@login_required
def create_blogpost():
    """
    View function for displaying new blogpost form
    """
    form = NewBlogpost()

    if form.validate_on_submit():
        title = form.title.data
        author = form.author.data
        post_content = form.post_content.data
        # image = form.image.data

        new_blogpost = Blogpost(title = title, author = author, user_id = current_user.id, body = post_content)

        db.session.add(new_blogpost)
        db.session.commit()

        return redirect(url_for("blogger.blogpost", blogpost_id = new_blogpost.id))

    title = "Unload - Create new post"
    return render_template('blogger/new_post.html', blogpost_form = form)

@blogger.route("/<user_name>/subscribers")
@login_required
def subscribers(user_name):
    """
    View function for displaying list of blogger's subscribers
    """
    pass

@login_required
@blogger.route("/pic", methods=["GET", "POST"])
def new_pic():
    user = User.query.filter_by(id = current_user.id).first()

    if 'photo' in request.files:
        print("\nUSER", user)
        filename = photos.save(request.files["photo"])
        path = f"static/images/profile_pics/{filename}"
        user.profile_pic_path = path
        db.session.commit()
        print("PROFILE PATH: ", user.profile_pic_path)

    return redirect(url_for("blogger.profile", user_name = current_user.user_name))