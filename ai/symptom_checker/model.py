import os
import json
from collections import defaultdict

class SymptomChecker:
    def __init__(self, data_path=None):
        dir_path = os.path.dirname(os.path.abspath(__file__))
        root_path = os.path.dirname(os.path.dirname(dir_path))
        data_path = data_path or os.path.join(root_path, 'data')
        self.data_path = data_path
        self.load_data()

    def load_data(self):
        with open(os.path.join(self.data_path, 'symptoms.json')) as f:
            self.symptoms = json.load(f)
        with open(os.path.join(self.data_path, 'conditions.json')) as f:
            self.conditions = json.load(f)
        with open(os.path.join(self.data_path, 'specialists.json')) as f:
            self.specialists = json.load(f)
        # Build quick lookup
        self.symptom_to_condition = defaultdict(list)
        for cond in self.conditions:
            for s in cond['symptoms']:
                self.symptom_to_condition[s].append(cond['id'])

    def analyze_symptoms(self, patient_symptoms, duration=None, severity=None):
        # Score conditions based on matched symptoms
        scores = []
        for cond in self.conditions:
            matched = set(cond['symptoms']) & set(patient_symptoms)
            if not matched:
                continue
            score = len(matched) / len(cond['symptoms'])
            if cond.get("primary_symptoms"):
                primary_matched = set(cond["primary_symptoms"]) & set(patient_symptoms)
                if primary_matched:
                    score += 0.2 * len(primary_matched)
            # Optionally adjust score based on input duration/severity
            if duration and "typical_duration" in cond and str(cond["typical_duration"]) == str(duration):
                score += 0.1
            if severity and "typical_severity" in cond and str(cond["typical_severity"]) == str(severity):
                score += 0.05
            scores.append({
                "condition": cond["name"],
                "description": cond["description"],
                "probability": round(min(score, 1.0), 2),
                "specialist": cond["specialist"],
                "matched_symptoms": list(matched),
                "severity": cond.get("typical_severity", "Moderate"),
            })
        # Sort by probability
        scores.sort(key=lambda x: x['probability'], reverse=True)
        return scores[:5]

    def get_specialist_recommendations(self, conditions):
        specialist_scores = defaultdict(float)
        for cond in conditions:
            specialist_scores[cond["specialist"]] += cond["probability"]
        recommendations = []
        for specialist, score in specialist_scores.items():
            spec = next((s for s in self.specialists if s["id"] == specialist), None)
            if spec:
                recommendations.append({
                    "name": spec["name"],
                    "description": spec["description"],
                    "score": round(score, 2)
                })
        recommendations.sort(key=lambda x: x["score"], reverse=True)
        return recommendations