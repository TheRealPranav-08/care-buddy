from utils.db import db
from datetime import datetime

class MedicalRecord(db.Model):
    __tablename__ = 'medical_records'
    
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patients.id'))
    record_type = db.Column(db.String(50), nullable=False)
    record_date = db.Column(db.Date, nullable=False)
    description = db.Column(db.Text)
    file_path = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'patient_id': self.patient_id,
            'record_type': self.record_type,
            'record_date': self.record_date.isoformat(),
            'description': self.description,
            'file_path': self.file_path,
            'created_at': self.created_at.isoformat()
        }
