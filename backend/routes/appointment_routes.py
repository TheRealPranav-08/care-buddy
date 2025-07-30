from flask import Blueprint, request, jsonify
from models.appointment import Appointment
from utils.db import db
from utils.auth import token_required
from datetime import datetime

bp = Blueprint('appointments', __name__, url_prefix='/appointments')

@bp.route('/', methods=['GET'])
@token_required
def get_appointments(current_user):
    if current_user.role == 'patient':
        appointments = Appointment.query.filter_by(patient_id=current_user.id).all()
    else:
        appointments = Appointment.query.filter_by(doctor_id=current_user.id).all()
    return jsonify([apt.to_dict() for apt in appointments])

@bp.route('/', methods=['POST'])
@token_required
def create_appointment(current_user):
    data = request.get_json()
    appointment = Appointment(
        patient_id=current_user.id if current_user.role == 'patient' else data['patient_id'],
        doctor_id=data['doctor_id'],
        appointment_date=datetime.strptime(data['appointment_date'], '%Y-%m-%d').date(),
        appointment_time=datetime.strptime(data['appointment_time'], '%H:%M').time(),
        reason=data.get('reason', '')
    )
    db.session.add(appointment)
    db.session.commit()
    return jsonify(appointment.to_dict()), 201

@bp.route('/<int:id>', methods=['PUT'])
@token_required
def update_appointment(current_user, id):
    appointment = Appointment.query.get_or_404(id)
    data = request.get_json()
    
    if 'status' in data:
        appointment.status = data['status']
    
    db.session.commit()
    return jsonify(appointment.to_dict())
