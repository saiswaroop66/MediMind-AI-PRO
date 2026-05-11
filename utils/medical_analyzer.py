import re

def analyze_report(text):

    results = []

    # Hemoglobin
    hemoglobin = re.search(
        r"Hemoglobin[:\s]+(\d+\.?\d*)",
        text,
        re.IGNORECASE
    )

    if hemoglobin:

        hb_value = float(hemoglobin.group(1))

        if hb_value < 13:
            results.append(f"⚠ Low Hemoglobin: {hb_value}")

        else:
            results.append(f"✅ Hemoglobin Normal: {hb_value}")

    # Blood Sugar
    sugar = re.search(
        r"Blood Sugar[:\s]+(\d+\.?\d*)",
        text,
        re.IGNORECASE
    )

    if sugar:

        sugar_value = float(sugar.group(1))

        if sugar_value > 140:
            results.append(f"⚠ High Blood Sugar: {sugar_value}")

        else:
            results.append(f"✅ Blood Sugar Normal: {sugar_value}")

    # Vitamin D
    vitamin_d = re.search(
        r"Vitamin D[:\s]+(\d+\.?\d*)",
        text,
        re.IGNORECASE
    )

    if vitamin_d:

        vd_value = float(vitamin_d.group(1))

        if vd_value < 30:
            results.append(f"⚠ Vitamin D Deficiency: {vd_value}")

        else:
            results.append(f"✅ Vitamin D Normal: {vd_value}")

    # Cholesterol
    cholesterol = re.search(
        r"Cholesterol[:\s]+(\d+\.?\d*)",
        text,
        re.IGNORECASE
    )

    if cholesterol:

        chol_value = float(cholesterol.group(1))

        if chol_value > 200:
            results.append(f"⚠ High Cholesterol: {chol_value}")

        else:
            results.append(f"✅ Cholesterol Normal: {chol_value}")

    return results
