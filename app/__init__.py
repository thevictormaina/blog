from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_mail import Mail
from flask_simplemde import SimpleMDE
from config import config_options
from .services.quote_request import configure_request

bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = "strong"
login_manager.login_view = "auth.login"
mail = Mail()
simple = SimpleMDE()
photos = UploadSet("photos", IMAGES)

def create_app(config_name):
    """
    Function for creating application
    """
    app = Flask(__name__)

    # Setting app configuration
    app.config.from_object(config_options[config_name])

    #Initialize app extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    simple.init_app(app)

    # Create UploadSet configuration
    configure_uploads(app, photos)

    # Register app blueprints
    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix="/auth")

    # Configure api requests
    configure_request(app)

    return app