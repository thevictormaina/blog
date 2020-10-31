from .. import db, login_manager
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

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