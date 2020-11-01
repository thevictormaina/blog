import unittest
from app.models import Blogpost, Comment
from app import db

class TestComment(unittest.TestCase):
    """
    Class for testing User properties and methods. Inherits from unittest.TestCase
    """
    def setUp(self):
        """
        Runs before each test
        """
        db.create_all()

        self.blogpost = Blogpost(title="How to Start a Blog")
        self.comment = Comment(full_name="Jane Doe", email = "janedoe@example.com", comment="Can't wait to start my own!", blogpost_id = 1)

        db.session.add_all([self.blogpost, self.comment])
        db.session.commit()

    def tearDown(self):
        """
        Runs after each test
        """
        db.session.commit()
        db.drop_all()

    def test_comment_instance(self):
        """
        Class to check if instance of Subscriber is created and committed to database
        """
        comment = Comment.query.first()

        self.assertEqual(comment.full_name, "Jane Doe")
        self.assertEqual(comment.email, "janedoe@example.com")
        self.assertEqual(comment.comment, "Can't wait to start my own!")
        self.assertEqual(comment.blogpost_id, 1)



    def test_delete_comment(self):
        """
        Test to check if delete_comment method removes comment from database
        """

        self.comment.delete_comment()

        self.assertFalse(Comment.query.first())