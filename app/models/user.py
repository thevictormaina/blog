from .. import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from .subscriber import subscriptions_table

@login_manager.user_loader
def load_user(user_id):
    """
    Return instance of current user

    Args:
        user_id: unique id of user
    """
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    """
    Class for defining users and user methods. Inherits from UserMixin and db.Model
    """ 
    __tablename__="users"
    id = db.Column(db.Integer, primary_key = True)
    user_name = db.Column(db.String(255), index = True)
    email = db.Column(db.String(255), index = True)
    pass_secure = db.Column(db.String())
    profile_pic_path = db.Column(db.String())
    first_name = db.Column(db.String(255))
    last_name = db.Column(db.String(255))
    headline = db.Column(db.String())
    bio = db.Column(db.String())
    
    blogposts = db.relationship("Blogpost", back_populates = "user")

    subscribers = db.relationship("Subscriber", secondary = subscriptions_table, back_populates="subscriptions")

    @property
    def password(self):
        """
        Raises AttributeError if password access is attempted
        """
        raise AttributeError("You cannot access the password.")

    @password.setter
    def password(self, password):
        """
        Generate password hash
        """
        self.pass_secure = generate_password_hash(password)

    def verify_password(self, password):
        """
        Method to validate password hash
        """
        return check_password_hash(self.pass_secure, password)

    def __repr__(self):
        return f"User {self.user_name}"