from .. import db

class Subscriber(db.Model):
    """
    Class for defining blogposts instances and methods. Inherits from db.Model.
    """ 
    __tablename__="subscribers"