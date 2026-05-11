# =========================================
# FILE: utils/health_score.py
# =========================================

def calculate_health_score(analysis):

    score = 100

    for item in analysis:

        if "Hemoglobin" in item:
            score -= 15

        elif "Blood Sugar" in item:
            score -= 20

        elif "Vitamin D" in item:
            score -= 10

        elif "Cholesterol" in item:
            score -= 20

    if score < 0:
        score = 0

    return score
