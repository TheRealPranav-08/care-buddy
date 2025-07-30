from flask import Flask, jsonify, render_template
from flask_login import LoginManager
from config import Config
from utils.db import db, init_db
from models.user import User
import os
from flask_cors import CORS  # Add this import for handling CORS

def create_app():
    app = Flask(__name__)
    CORS(app)  # Enable CORS for all routes
    app.config.from_object(Config)
    
    # Ensure upload folder exists
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
    
    # Initialize extensions
    db.init_app(app)
    login_manager = LoginManager()
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    # Import and register blueprints
    from routes.auth_routes import bp as auth_bp
    from routes.patient_routes import bp as patient_bp
    from routes.appointment_routes import bp as appointment_bp
    from routes.file_routes import bp as file_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(patient_bp)
    app.register_blueprint(appointment_bp)
    app.register_blueprint(file_bp)
    
    @app.route('/')
    def index():
        return jsonify({
            "message": "Welcome to Smart Healthcare Portal API",
            "status": "running",
            "current_time": "2025-07-30 11:14:36",
            "user": "7puteyash",
            "endpoints": {
                "auth": "/auth",
                "patients": "/patients",
                "appointments": "/appointments",
                "files": "/files"
            }
        })
    
    @app.route('/health')
    def health_check():
        return jsonify({'status': 'healthy'})
    
    # Create database tables
    with app.app_context():
        db.create_all()
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)