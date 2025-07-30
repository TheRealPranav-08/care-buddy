import pytest
import main

@pytest.fixture
def client():
    main.app.config['TESTING'] = True
    with main.app.test_client() as client:
        yield client

def test_doctors(client):
    rv = client.get('/api/doctors')
    assert rv.status_code == 200
    data = rv.get_json()
    assert isinstance(data, list)
    assert any('name' in d for d in data)

def test_symptom_checker(client):
    rv = client.post('/api/symptoms', json={"symptoms": ["fever", "cough"]})
    assert rv.status_code == 200
    data = rv.get_json()
    assert 'diagnosis' in data

def test_book_appointment(client):
    rv = client.post('/api/appointments', json={
        "name": "Test User",
        "email": "test@email.com",
        "date": "2025-08-01",
        "time": "10:00",
        "doctor": "Dr. Alice Smith"
    })
    assert rv.status_code == 200
    data = rv.get_json()
    assert 'message' in data