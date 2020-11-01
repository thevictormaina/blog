import unittest
from app.models import User, Subscriber
from app.models.subscriber import subscriptions_table
from app import db

class TestSubscriber(unittest.TestCase):
    """
    Class for testing User properties and methods. Inherits from unittest.TestCase
    """
    def setUp(self):
        """
        Runs before each test
        """
        db.create_all()

        self.subscriber = Subscriber(email="johndoe@example.com", first_name="John", last_name="Doe")
        self.user = User(user_name="victormainak")

    def tearDown(self):
        """
        Runs after each test
        """
        db.session.commit()
        db.drop_all()

    def test_subscriber_instance(self):
        """
        Class to check if instance of Subscriber is created and committed to database
        """
        db.session.add_all([self.subscriber, self.user])
        db.session.commit()

        sub = Subscriber.query.filter_by(email = "johndoe@example.com").first()

        self.assertEqual(sub.email, "johndoe@example.com")
        self.assertEqual(sub.first_name, "John")
        self.assertEqual(sub.last_name, "Doe")

    def test_subscriptions(self):
        """
        Test to check if subscriptions property is being populated by User instances
        """
        db.session.add_all([self.subscriber, self.user])
        db.session.commit()

        self.subscriber.subscriptions.append(self.user)

        print("Subscribers: ", self.user.subscribers)

        self.assertTrue(len(Subscriber.query.filter_by(email="johndoe@example.com").first().subscriptions) > 0)

    def test_add_subscription(self):
        """
        Test case to see if add_subscription appends user to Subscriber.subscriptions
        """
        db.session.add_all([self.subscriber, self.user])
        db.session.commit()

        self.subscriber.add_subscription(self.user)

        self.assertEqual(Subscriber.query.first().subscriptions[0], self.user)
        self.assertEqual(User.query.first().subscribers[0], self.subscriber)
