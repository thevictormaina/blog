from .. import db

class Blogpost(db.Model):
    """
    Class for defining blogposts instances and methods. Inherits from db.Model.
    """ 
    __tablename__="blogposts"