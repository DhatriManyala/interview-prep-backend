from flask import request, jsonify
from flask_jwt_extended import jwt_required
from models import PracticeQuestion
from flask import Blueprint

practice_bp = Blueprint('practice', __name__)

@practice_bp.route('/questions', methods=['GET'])
@jwt_required()
def get_practice_questions():
    questions = PracticeQuestion.query.all()
    result = [{"id": q.id, "question": q.question, "answer": q.answer} for q in questions]
    return jsonify(result), 200