from flask import jsonify
from flask_jwt_extended import jwt_required
from models import Flashcard
from flask import Blueprint

flashcards_bp = Blueprint('flashcards', __name__)

@flashcards_bp.route('/all', methods=['GET'])
@jwt_required()
def get_flashcards():
    cards = Flashcard.query.all()
    result = [{"id": c.id, "front": c.front, "back": c.back} for c in cards]
    return jsonify(result), 200