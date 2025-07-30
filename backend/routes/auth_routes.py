from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash
from models.user import User
from utils.db import db
from utils.auth import generate_token

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/test', methods=['GET'])
def test():
    return jsonify({'message': 'Auth routes working'})

# ... rest of your auth routes ...