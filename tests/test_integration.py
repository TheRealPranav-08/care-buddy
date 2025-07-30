import main

def test_full_flow():
    app = main.app
    app.config['TESTING'] = True
    with app.test_client() as c:
        # 1. Get doctors
        res = c.get('/api/doctors')
        assert res.status_code == 200
        doctors = res.get_json()
        assert len(doctors) > 0
        doctor = doctors[0]['name']

        # 2. Book appointment
        appt = {
            "name": "Integration Test",
            "email": "int@test.com",
            "date": "2025-08-01",
            "time": "11:00",
            "doctor": doctor
        }
        res = c.post('/api/appointments', json=appt)
        assert res.status_code == 200

        # 3. List appointments
        res = c.get('/api/appointments')
        assert res.status_code == 200
        appts = res.get_json()
        assert any(a['name'] == "Integration Test" for a in appts)