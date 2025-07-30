from flask import Blueprint, request, jsonify, current_app
from werkzeug.utils import secure_filename
from models.medical import MedicalRecord
from utils.db import db
from utils.auth import token_required
import os
from datetime import datetime

bp = Blueprint('files', __name__, url_prefix='/files')

def allowed_file(filename):
    ALLOWED_EXTENSIONS = {'pdf', 'png', 'jpg', 'jpeg', 'doc', 'docx'}
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@bp.route('/upload', methods=['POST'])
@token_required
def upload_file(current_user):
    if 'file' not in request.files:
        return jsonify({'message': 'No file part'}), 400
        
    file = request.files['file']
    if file.filename == '':
        return jsonify({'message': 'No selected file'}), 400
        
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        record = MedicalRecord(
            patient_id=request.form.get('patient_id'),
            record_type=request.form.get('record_type'),
            record_date=datetime.now().date(),
            description=request.form.get('description'),
            file_path=filepath
        )
        
        db.session.add(record)
        db.session.commit()
        
        return jsonify(record.to_dict()), 201
        
    return jsonify({'message': 'File type not allowed'}), 400