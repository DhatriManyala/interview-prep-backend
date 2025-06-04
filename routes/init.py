from flask import Blueprint

# Define blueprints here
auth_bp = Blueprint('auth', __name__)
practice_bp = Blueprint('practice', __name__)
quiz_bp = Blueprint('quiz', __name__)
flashcards_bp = Blueprint('flashcards', __name__)
mock_interview_bp = Blueprint('mock_interview', __name__)

# Import the route modules that register routes on these blueprints
from . import auth
from . import practice
from . import quiz
from . import flashcards
from . import mock_interview