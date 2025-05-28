# ml_model.py

import difflib

class AnswerEvaluator:
    def _init_(self):
        # Initialize your ML model here if you want to extend in future
        pass

    def evaluate(self, question_text: str, user_answer: str) -> dict:
        """
        Evaluate the user's answer compared to the question text.
        Uses simple similarity ratio via difflib.SequenceMatcher.

        Returns:
            dict: {
                'score': float (0.0 to 1.0),
                'feedback': str
            }
        """
        question_text = question_text.lower()
        user_answer = user_answer.lower()

        # Calculate similarity ratio
        similarity = difflib.SequenceMatcher(None, question_text, user_answer).ratio()

        # Thresholds for feedback
        if similarity > 0.7:
            feedback = "Great job! Your answer is very relevant."
        elif similarity > 0.4:
            feedback = "Good attempt, but you can add more details."
        else:
            feedback = "Your answer seems off-topic. Try to focus more on the question."

        return {
            "score": round(similarity, 2),
            "feedback": feedback
        }

# Singleton instance to use in backend routes
answer_evaluator = AnswerEvaluator()