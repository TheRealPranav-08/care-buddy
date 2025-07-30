from flask import Blueprint, request, jsonify
from models.patient import Patient
from utils.db import db
from utils.auth import token_required, role_required

bp = Blueprint('patients', __name__, url_prefix='/patients')

@bp.route('/', methods=['GET'])
@token_required
def get_patients(current_user):
    if current_user.role != 'doctor':
        patients = Patient.query.filter_by(user_id=current_user.id).all()
    else:
        patients = Patient.query.all()
    return jsonify([patient.to_dict() for patient in patients])

@bp.route('/<int:id>', methods=['GET'])
@token_required
def get_patient(current_user, id):
    patient = Patient.query.get_or_404(id)
    return jsonify(patient.to_dict())

@bp.route('/', methods=['POST'])
@token_required
def create_patient(current_user):
    data = request.get_json()
    patient = Patient(
        user_id=current_user.id,
        first_name=data['first_name'],
        last_name=data['last_name'],
        date_of_birth=data['date_of_birth'],
        gender=data.get('gender'),
        blood_group=data.get('blood_group'),
        contact_number=data.get('contact_number'),
        address=data.get('address')
    )
    db.session.add(patient)
    db.session.commit()
    return jsonify(patient.to_dict()), 201