import unittest
from app.models import User, Blogpost, Comment
from app import db

class TestBlogpost(unittest.TestCase):
    """
    Class for testing Blogpost properties and methods. Inherits from unittest.TestCase
    """
    def setUp(self):
        """
        Runs before each test
        """
        db.create_all()

        self.blogpost = Blogpost(author="Victor Maina", user_id=1, title="5 Ways to Get Rid of Tough Stains", body="Lorem ipsum...", post_image_path="/path/to/image/", upvotes=3)
        self.user = User(user_name="johndoe", first_name="John", last_name="Doe")

        db.session.add_all([self.blogpost, self.user])
        db.session.commit()

    def tearDown(self):
        """
        Runs after each test
        """
        db.session.commit()
        db.drop_all()

    def test_blogpost_instance(self):
        """
        Class to check if instance of Blogpost is created and committed to database
        """
        user = User.query.first()
        blogpost = Blogpost.query.first()

        self.assertEqual(blogpost.author, "Victor Maina")
        self.assertEqual(blogpost.user_id, 1)
        self.assertEqual(blogpost.title, "5 Ways to Get Rid of Tough Stains")
        self.assertEqual(blogpost.body, "Lorem ipsum...")
        self.assertEqual(blogpost.post_image_path, "/path/to/image/")
        self.assertEqual(blogpost.upvotes, 3)
        

    def test_comments(self):
        """
        Test to check if comments property is being populated by Comment instances
        """
        comment = Comment(full_name="Jane Doe", comment="Very informative")
        db.session.add(comment)
        db.session.commit()

        self.blogpost.comments.append(comment)

        self.assertEqual(Blogpost.query.first().comments[0], comment)

    def test_self_author(self):
        """
        Test case to check is self_author method sets author attribute to user's first and last names
        """
        blogpost = Blogpost.query.first()
        user = User.query.first()
        author_name = f"{user.first_name} {user.last_name}"

        blogpost.self_author()

        self.assertEqual(blogpost.author, author_name)

    def test_delete_post(self):
        """
        Test case to check if delete_post method removes blogpost from database
        """
        self.blogpost.delete_post()
        print(Blogpost.query.all())

        self.assertFalse(Blogpost.query.first())