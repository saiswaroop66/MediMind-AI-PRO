# =========================================
# FILE: utils/symptom_analyzer.py
# =========================================

def analyze_symptoms(text):

    symptom_results = []

    text = text.lower()

    symptom_conditions = {

        "fever": {
            "condition": "Viral Fever / Infection",
            "doctor": "General Physician"
        },

        "cough": {
            "condition": "Respiratory Infection",
            "doctor": "Pulmonologist"
        },

        "headache": {
            "condition": "Migraine / Stress",
            "doctor": "Neurologist"
        },

        "chest pain": {
            "condition": "Possible Heart Issue",
            "doctor": "Cardiologist"
        },

        "fatigue": {
            "condition": "Weakness / Vitamin Deficiency",
            "doctor": "General Physician"
        },

        "breathing problem": {
            "condition": "Respiratory Disorder",
            "doctor": "Pulmonologist"
        },

        "vomiting": {
            "condition": "Food Poisoning / Infection",
            "doctor": "General Physician"
        },

        "dizziness": {
            "condition": "Blood Pressure / Weakness Issue",
            "doctor": "Neurologist"
        },

        "stomach pain": {
            "condition": "Gastric / Digestive Issue",
            "doctor": "Gastroenterologist"
        },

        "diabetes": {
            "condition": "Blood Sugar Disorder",
            "doctor": "Endocrinologist"
        },

        "cold": {
            "condition": "Common Cold / Viral Infection",
            "doctor": "General Physician"
        },

        "high bp": {
            "condition": "Hypertension",
            "doctor": "Cardiologist"
        }

    }

    for symptom, info in symptom_conditions.items():

        if symptom in text:

            symptom_results.append(
                f"⚠ Symptom Detected: {symptom.title()}"
            )

            symptom_results.append(
                f"🩺 Possible Condition: {info['condition']}"
            )

            symptom_results.append(
                f"👨‍⚕ Recommended Doctor: {info['doctor']}"
            )

    emergency_symptoms = [
        "chest pain",
        "breathing problem",
        "high bp"
    ]

    for emergency in emergency_symptoms:

        if emergency in text:

            symptom_results.append(
                f"🚨 Emergency Attention Recommended for: {emergency.title()}"
            )

    return symptom_results
