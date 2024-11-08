import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    """
    Class for app configuration
    """
    # WTForms configurations
    SECRET_KEY = os.getenv("SECRET_KEY")

    # Set location for Flask Uploads
    UPLOADED_PHOTOS_DEST = "app/static/images/profile_pics"

    # API Key configurations
    QUOTE_URL = "http://quotes.stormconsultancy.co.uk/random.json"
    # Mail configurations
    MAIL_SERVER = os.getenv("MAIL_SERVER")
    MAIL_PORT = os.getenv("MAIL_PORT")
    MAIL_USE_TLS = os.getenv("MAIL_USE_TLS")
    MAIL_USERNAME = os.getenv("MAIL_USERNAME")
    MAIL_PASSWORD = os.getenv("MAIL_PASSWORD")

    # SimpleMDE Configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USER_CDN = True


class DevConfig(Config):
    """
    Class for development configurations. Child of class Config.
    """
    DB_USERNAME = os.getenv("DB_USERNAME")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_NAME = os.getenv("DB_NAME")
    DB_HOST = os.getenv("DB_HOST")
    SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"
    DEBUG = os.getenv("APPLICATION_DEBUG") == "True"


class TestConfig(Config):
    """
    Class for testing configurations. Child of class Config.
    """
    DB_USERNAME = os.getenv("DB_USERNAME")
    DB_PASSWORD = os.getenv("DB_PASSWORD")
    DB_NAME = os.getenv("DB_NAME")
    DB_HOST = os.getenv("DB_HOST")
    SQLALCHEMY_DATABASE_URI = f"postgresql+psycopg2://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/blog_app_test"


class ProdConfig(Config):
    """
    Class for production configurations. Child of class Config.
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


config_options = {
    "development": DevConfig,
    "test": TestConfig,
    "production": ProdConfig
}
