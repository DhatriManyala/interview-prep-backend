from flask import Blueprint

auth_bp = Blueprint('auth', __name__)
practice_bp = Blueprint('practice', __name__)
quiz_bp = Blueprint('quiz', __name__)
flashcards_bp = Blueprint('flashcards', __name__)
mock_interview_bp = Blueprint('mock_interview', __name__)

from .auth import *
from .practice import *
from .quiz import *
from .flashcards import *
from .mock_interview import *