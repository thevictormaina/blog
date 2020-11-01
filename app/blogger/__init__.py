from flask import Blueprint

blogger = Blueprint("blogger", __name__)

from . import views, forms