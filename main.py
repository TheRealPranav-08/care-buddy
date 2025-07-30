from flask import Flask, render_template, request, jsonify
from scripts.seed_db import seed_database
import sqlite3
import os

app = Flask(__name__, template_folder='templates')

DATABASE = 'healthcare.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/symptoms', methods=['POST'])
def check_symptoms():
    data = request.get_json()
    symptoms = data.get('symptoms', [])
    # Simple symptom checker mockup
    # In reality, call AI/ML model here
    if "fever" in symptoms and "cough" in symptoms:
        return jsonify({'diagnosis': 'Possible Flu', 'advice': 'Rest, stay hydrated, consult doctor if worsens.'})
    elif "headache" in symptoms:
        return jsonify({'diagnosis': 'Possible Migraine', 'advice': 'Rest, avoid bright lights, consult doctor.'})
    else:
        return jsonify({'diagnosis': 'Unknown', 'advice': 'Please consult a doctor.'})

@app.route('/api/appointments', methods=['GET', 'POST'])
def appointments():
    conn = get_db_connection()
    if request.method == 'POST':
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        date = data.get('date')
        time = data.get('time')
        doctor = data.get('doctor')
        conn.execute('INSERT INTO appointments (name, email, date, time, doctor) VALUES (?, ?, ?, ?, ?)',
                     (name, email, date, time, doctor))
        conn.commit()
        conn.close()
        return jsonify({'message': 'Appointment booked successfully!'})
    else:
        appts = conn.execute('SELECT * FROM appointments').fetchall()
        conn.close()
        return jsonify([dict(a) for a in appts])

@app.route('/api/doctors', methods=['GET'])
def doctors():
    conn = get_db_connection()
    docs = conn.execute('SELECT * FROM doctors').fetchall()
    conn.close()
    return jsonify([dict(d) for d in docs])

if __name__ == '__main__':
    if not os.path.exists(DATABASE):
        seed_database(DATABASE)
    app.run(debug=True)
