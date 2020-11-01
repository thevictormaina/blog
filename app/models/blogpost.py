from .. import db

class Blogpost(db.Model):
    """
    Class for defining blogposts instances and methods. Inherits from db.Model.
    """ 
    __tablename__="blogposts"
    id = db.Column(db.Integer, primary_key = True)
    author = db.Column(db.String(), index = True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    title = db.Column(db.String())
    body = db.Column(db.String())
    post_image_path = db.Column(db.String())
    upvotes = db.Column(db.Integer())

    user = db.relationship("User", back_populates = "blogposts")
    comments = db.relationship("Comment", backref="blogpost")