from flask import Blueprint

employment_bp = Blueprint('employment', __name__)

from . import routes