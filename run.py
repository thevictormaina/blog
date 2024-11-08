from app import create_app, db
from flask_script import Manager, Server
from flask_migrate import Migrate, MigrateCommand
from app.models import User, Blogpost, Comment, Subscriber
from dotenv import load_dotenv
import os

load_dotenv()

APPLICATION_MODE = os.getenv("APPLICATION_MODE")

mode = APPLICATION_MODE if APPLICATION_MODE is not None else "development"
# Create app instance
app = create_app(mode)

# Initialize Manager extension and create server CLI command
manager = Manager(app)
manager.add_command("server", Server)

# Initialize Migrate extension and create migration CLI commands
migrate = Migrate(app, db, include_schemas=True)
manager.add_command("db", MigrateCommand)


# Create CLI commands for running tests
# @manager.command
# def test():
#     """
#     Function for running unit tests
#     """
#     import unittest
#     tests = unittest.TestLoader().discover("tests")
#     unittest.TextTestRunner(verbosity=2).run(tests)

# Define CLI command for creating Python shell environment


@manager.shell
def shell_environment():
    return dict(app=app, db=db, User=User, Comment=Comment, Subscriber=Subscriber, Blogpost=Blogpost)


# Run application
if __name__ == "__main__":
    manager.run()
