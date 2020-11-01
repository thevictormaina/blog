from flask import flash, redirect, render_template, request, url_for
from flask_login import login_required, login_user, logout_user
from sqlalchemy import or_

from ..models import User
from ..services.email import mail_message
from . import auth
from .forms import CreateAccountForm, LoginForm
from .. import db

@auth.route("/login", methods=["GET", "POST"])
def login():
    """
    View function for returning login page
    """
    login_form = LoginForm()

    if login_form.validate_on_submit():
        user = User.query.filter(or_(User.user_name == login_form.username_email.data)).first()
        if user is not None and user.verify_password(login_form.password.data):
            login_user(user, login_form.remember.data)
            return redirect(request.args.get("next") or url_for("main.index"))
        
        flash("Invalid username or password")

    title = "Unloaded - Log In"
    return render_template("auth/login.html", login_form = login_form, title = title)

@auth.route("/sign-out", methods=["GET", "POST"])
@login_required
def logout():
    """
    View function for logging out
    """
    logout_user()
    return redirect(url_for("main.index"))

@auth.route("/create-account", methods=["GET", "POST"])
def sign_in():
    form = CreateAccountForm()

    if form.validate_on_submit():
        user = User(user_name = form.username.data, email = form.email.data, password = form.password.data, first_name = form.first_name.data, last_name = form.last_name.data)
        db.session.add(user)
        db.session.commit()


        mail_message("Welcome to Unload", "email/welcome_email", user.email, user = user)

        return redirect(url_for("auth.login"))
        title = "Unload - Create New Account"

    return render_template("auth/create_account.html", create_account_form = form)