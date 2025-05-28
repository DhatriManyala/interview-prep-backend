# Flask secret key (random 64 hex chars)
SECRET_KEY=4e3f2b8c9a7d6e5f1b2c3d4e5f67890123456789abcdef0123456789abcdef

# JWT secret key (random 64 hex chars)
JWT_SECRET_KEY=9f8e7d6c5b4a39281736455463728190abcdef1234567890abcdef1234567890

# Database URI (replace dbuser, dbpassword, hostname, dbname)
SQLALCHEMY_DATABASE_URI=postgresql://dbuser:dbpassword@localhost:5432/interviewprepdb

# SMTP Settings (replace with your AWS SES or other SMTP service credentials)
MAIL_SERVER=email-smtp.us-east-1.amazonaws.com
MAIL_PORT=587
MAIL_USE_TLS=True
MAIL_USERNAME=AKIAIOSFODNN7EXAMPLE   # Replace with your SMTP user
MAIL_PASSWORD=your_smtp_password_here
MAIL_DEFAULT_SENDER=verified_email@example.com

# Flask environment mode
FLASK_ENV=production