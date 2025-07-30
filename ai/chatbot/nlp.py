def extract_symptoms(message):
    # Very basic keyword-based extraction
    keywords = [
        "fever", "headache", "cough", "fatigue", "sore throat", "shortness of breath",
        "chest pain", "nausea", "vomiting", "diarrhea", "body ache", "rash", "dizziness", "chills",
        "runny nose", "stomach pain", "joint pain", "loss of appetite", "weight loss", "swelling"
    ]
    found = []
    msg = message.lower()
    for k in keywords:
        if k in msg:
            found.append(k.replace(" ", "_"))
    return found