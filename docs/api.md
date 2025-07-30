# API Documentation

## POST `/api/symptoms`
- Input: `{ "symptoms": ["fever", "cough"] }`
- Output: `{ "diagnosis": "...", "advice": "..." }`

## GET, POST `/api/appointments`
- GET: List all appointments
- POST: Book new appointment
    - Input: `{ "name": "...", "email": "...", "date": "...", "time": "...", "doctor": "..." }`

## GET `/api/doctors`
- Lists all available doctors
