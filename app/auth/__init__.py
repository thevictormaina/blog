from flask import Blueprint

main = Flask(__name__)

from . import views, forms