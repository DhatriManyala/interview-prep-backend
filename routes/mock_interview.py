from flask import jsonify
from flask_jwt_extended import jwt_required
from models import MockInterviewQuestion
from flask import Blueprint

mock_interview_bp = Blueprint('mock_interview', _name_)

@mock_interview_bp.route('/questions', methods=['GET'])
@jwt_required()
def get_mock_interview_questions():
    questions = MockInterviewQuestion.query.all()
    result = [{"id": q.id, "question": q.question, "answer": q.answer} for q in questions]
    return jsonify(result), 200