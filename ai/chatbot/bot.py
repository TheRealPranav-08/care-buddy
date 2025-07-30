from .responses import get_response_templates
from .nlp import extract_symptoms
import random

class MedicalChatBot:
    def __init__(self):
        self.templates = get_response_templates()
        self.context = {"name": None, "symptoms": [], "previous": None}

    def process_message(self, message):
        # Extract symptoms if mentioned
        syms = extract_symptoms(message)
        for s in syms:
            if s not in self.context["symptoms"]:
                self.context["symptoms"].append(s)
        # Greeting
        if any(word in message.lower() for word in ["hello", "hi", "hey"]):
            return random.choice(self.templates['greeting'])
        # Thank you
        if "thank" in message.lower():
            return random.choice(self.templates['thanks'])
        # If asking about a disease
        for cond in ["cold", "flu", "covid"]:
            if cond in message.lower():
                return random.choice(self.templates['condition']).replace("{condition}", cond.title())
        # If symptom description
        if self.context["symptoms"]:
            response = random.choice(self.templates["symptom_description"])
            return response.replace("{symptoms}", ", ".join(self.context["symptoms"]))
        # General fallback
        return random.choice(self.templates["general"])