from .. import db

class Comment(db.Model):
    """
    Class for defining comment instances and methods. Inherits from db.Model.
    """ 
    __tablename__="comments"