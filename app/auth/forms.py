import email_validator
from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import Email, EqualTo, Required

from ..models import User


class CreateAccountForm(FlaskForm):
    """
    Class to make form for creating new account
    """
    first_name = StringField("First name", validators=[Required()])
    last_name = StringField("Last name", validators=[Required()])
    username = StringField("Username", validators=[Required()])
    email = StringField("Email address", validators=[Required(), Email()])
    password = PasswordField("Password", validators=[Required(), EqualTo("password_confirm", message="Password must match.")])
    password_confirm = PasswordField("confirm password", validators=[Required()])
    submit = SubmitField("Create Account")

    def validate_email(self, data_field):
        """
        Method to check database and raise error if same email is found
        """
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError("There is an account with that email address.")

    def validate_username(self, data_field):
        """
        Method to check database and raise error if same email is found
        """
        if User.query.filter_by(user_name = data_field.data).first():
            raise ValidationError("That username is taken.")

class LoginForm(FlaskForm):
    """
    Class to define form for user login
    """
    username_email = StringField("Username or email address", validators=[Required()])
    password = PasswordField("Password", validators=[Required()])
    remember = BooleanField("Remember Me")
    submit = SubmitField("Log In")