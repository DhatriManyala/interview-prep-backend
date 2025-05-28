import os
from flask import Flask
from dotenv import load_dotenv

from extensions import db, migrate, jwt, bcrypt, mail, cors, limiter, talisman
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

# 3. Initialize extensions (AFTER config is loaded)
cors.init_app(app)
talisman.init_app(app)
db.init_app(app)
migrate.init_app(app, db)
jwt.init_app(app)
bcrypt.init_app(app)
mail.init_app(app)
limiter.init_app(app)

# 4. Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(practice_bp)
app.register_blueprint(quiz_bp)
app.register_blueprint(flashcards_bp)
app.register_blueprint(mock_interview_bp)

# 5. Create tables if they don't exist (optional)
@app.before_first_request
def create_tables():
    db.create_all()

# 6. Run the app
if __name__ == "_main_":
    app.run(debug=True)