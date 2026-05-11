import re

def analyze_medicines(text):

    medicine_results = []

    emergency_medicines = [
        "insulin",
        "warfarin",
        "epinephrine",
        "nitroglycerin",
        "aspirin"
    ]

    timing_pattern = r"([A-Za-z0-9\s]+)\s*-\s*(\d-\d-\d)"

    medicines = re.findall(timing_pattern, text)

    medicine_names = []

    for med_name, timing in medicines:

        med_name = med_name.strip()

        medicine_names.append(med_name.lower())

        medicine_results.append(
            f"💊 {med_name} Timing: {timing}"
        )

        # Emergency medicine detection
        for emergency in emergency_medicines:

            if emergency in med_name.lower():

                medicine_results.append(
                    f"🚨 Emergency Medicine Detected: {med_name}"
                )

    # Duplicate medicine detection
    duplicates = set()

    for med in medicine_names:

        if medicine_names.count(med) > 1:
            duplicates.add(med)

    for dup in duplicates:

        medicine_results.append(
            f"⚠ Duplicate Medicine Warning: {dup.title()}"
        )

    return medicine_results
