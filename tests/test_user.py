import unittest
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from app.models import User, Blogpost, Subscriber
from app.models.subscriber import subscriptions_table

class TestUser(unittest.TestCase):
    """
    Class for testing User properties and methods. Inherits from unittest.TestCase
    """
    def setUp(self):
        """
        Runs before each test
        """
        db.create_all()

        self.user = User(user_name="john_doe", email="johndoe@example.com", password="password", profile_pic_path="app/static/images", first_name="John", last_name="Doe", headline="Food Blogger", bio="Mainly writes on Chinese cuisine")

    def tearDown(self):
        """
        Runs after each test
        """
        db.session.commit()
        db.drop_all()

    def test_user_instance(self):
        """
        Test cases to check if user instance is created and commited correctly
        """
        db.session.add(self.user)
        db.session.commit()

        user = User.query.filter_by(user_name = "john_doe").first()
        users = User.query.all()

        self.assertTrue(len(users) > 0)
        self.assertEqual(user.user_name, "john_doe")
        self.assertEqual(user.email, "johndoe@example.com")
        self.assertEqual(user.profile_pic_path, "app/static/images")
        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Doe")
        self.assertEqual(user.headline, "Food Blogger")
        self.assertEqual(user.bio, "Mainly writes on Chinese cuisine")

    def test_verify_password(self):
        """
        Test case to check if password is verified"
        """
        db.session.add(self.user)
        db.session.commit()

        user = User.query.filter_by(user_name = "john_doe").first()

        self.assertTrue(user.verify_password("password"))
        self.assertFalse(user.verify_password("pass"))

    def test_blogposts(self):
        """
        Test case to check if blogposts property is created
        """
        db.session.add(self.user)
        db.session.commit()

        blogpost = Blogpost(author = "Jane Doe", user_id = 1)
        db.session.add(blogpost)
        db.session.commit()

        self.assertTrue(len(self.user.blogposts) > 0)

    def test_subscribers(self):
        """
        Test case to check if subscribers property is created
        """
        db.session.add(self.user)
        db.session.commit()

        sub = Subscriber(email = "janedoe@example.com")
        sub.subscriptions.append(self.user)
        db.session.add(sub)
        db.session.commit()

        self.assertTrue(len(self.user.subscribers) > 0)
