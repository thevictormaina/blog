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

    def self_author(self):
        """
        Method to set author as first and last name of user
        """
        from . import User
        user = User.query.filter_by(id = self.user_id).first()

        self.author = f"{user.first_name} {user.last_name}"

    def delete_post(self):
        """
        Method to delete blogpost
        """
        Blogpost.query.filter_by(id = self.id).delete()