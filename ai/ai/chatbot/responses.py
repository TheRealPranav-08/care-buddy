def get_response_templates():
    return {
        "greeting": [
            "Hello! How can I help you today?",
            "Hi there! Tell me your health concern.",
            "Greetings! What symptoms are you experiencing?"
        ],
        "thanks": [
            "You're welcome! Stay healthy.",
            "Glad I could help. If you have more questions, ask anytime!"
        ],
        "condition": [
            "You asked about {condition}. It's best to consult a doctor if symptoms persist.",
            "{condition} is common. Would you like to check your symptoms?"
        ],
        "symptom_description": [
            "You mentioned {symptoms}. Would you like to analyze them with our AI Symptom Checker?",
            "I see your symptoms: {symptoms}. Please use the symptom checker for a detailed analysis."
        ],
        "general": [
            "I'm your AI healthcare assistant. Please describe your symptoms or ask a medical question.",
            "Sorry, I didn't understand. Could you clarify or use the symptom checker?"
        ]
    }