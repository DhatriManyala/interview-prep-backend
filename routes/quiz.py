from flask import request, jsonify
from flask_jwt_extended import jwt_required
from models import QuizQuestion
from flask import Blueprint

quiz_bp = Blueprint('quiz', _name_)

@quiz_bp.route('/questions', methods=['GET'])
@jwt_required()
def get_quiz_questions():
    questions = QuizQuestion.query.all()
    result = []
    for q in questions:
        result.append({
            "id": q.id,
            "question": q.question,
            "options": q.options
        })
    return jsonify(result), 200