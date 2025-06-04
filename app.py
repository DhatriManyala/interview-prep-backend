import os
from flask import Flask, jsonify
from dotenv import load_dotenv
import redis
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from extensions import db, migrate, jwt, bcrypt, mail, cors, talisman
from config import Config
from routes.auth import auth_bp
from routes.practice import practice_bp
from routes.quiz import quiz_bp
from routes.flashcards import flashcards_bp
from routes.mock_interview import mock_interview_bp

# 1. Load environment variables
load_dotenv()

# 2. Create Flask app
app = Flask(__name__)
app.config.from_object(Config)

# 3. Initialize extensions
cors.init_app(app)
talisman.init_app(app)
db.init_app(app)
migrate.init_app(app, db)
jwt.init_app(app)
bcrypt.init_app(app)
mail.init_app(app)

# 4. Connect to Redis for Flask-Limiter
redis_client = redis.Redis(host='localhost', port=6379, db=0)

# 5. Initialize Flask-Limiter with Redis storage backend
limiter = Limiter(
    app,
    key_func=get_remote_address,
    storage_uri="redis://localhost:6379"
)

# 6. Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(practice_bp)
app.register_blueprint(quiz_bp)
app.register_blueprint(flashcards_bp)
app.register_blueprint(mock_interview_bp)

import models

# 7. Create tables (run once when app starts)
with app.app_context():
    db.create_all()

# 8. Test DB route
@app.route('/test-db')
def test_db():
    try:
        db.session.execute('SELECT 1')
        return jsonify({"message": "Database connection successful!"}), 200
    except Exception as e:
        return jsonify({"message": "Database connection failed", "error": str(e)}), 500

# 9. Run the app
if __name__ == '__main__':
    app.run(debug=True)