from flask import Blueprint

auth_bp = Blueprint('auth', _name_)
practice_bp = Blueprint('practice', _name_)
quiz_bp = Blueprint('quiz', _name_)
flashcards_bp = Blueprint('flashcards', _name_)
mock_interview_bp = Blueprint('mock_interview', _name_)

from .auth import *
from .practice import *
from .quiz import *
from .flashcards import *
from .mock_interview import *