from flask import Flask, request, jsonify
from symptom_checker.model import SymptomChecker
from chatbot.bot import MedicalChatBot

app = Flask(__name__)

# Instantiate AI modules
symptom_checker = SymptomChecker()
chatbot = MedicalChatBot()

@app.route('/api/symptom-check', methods=['POST'])
def symptom_check():
    data = request.json
    symptoms = data.get('symptoms', [])
    duration = data.get('duration')
    severity = data.get('severity')
    if not symptoms:
        return jsonify({"error": "Please provide symptoms."}), 400
    conditions = symptom_checker.analyze_symptoms(symptoms, duration, severity)
    specialists = symptom_checker.get_specialist_recommendations(conditions) if conditions else []
    return jsonify({
        "conditions": conditions,
        "specialists": specialists
    })

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.json
    message = data.get('message', '')
    if not message:
        return jsonify({"error": "Message is required."}), 400
    reply = chatbot.process_message(message)
    return jsonify({"response": reply})

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)