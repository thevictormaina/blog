from .. import db

class Comment(db.Model):
    """
    Class for defining comment instances and methods. Inherits from db.Model.
    """ 
    __tablename__="comments"
    id = db.Column(db.Integer, primary_key = True)
    full_name = db.Column(db.String())
    email = db.Column(db.String(255))
    comment = db.Column(db.String())
    blogpost_id = db.Column(db.Integer, db.ForeignKey("blogposts.id"))