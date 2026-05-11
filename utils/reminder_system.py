import re

def generate_reminders(text):

    reminders = []

    # Find medicines with timing pattern
    medicines = re.findall(
        r"([A-Za-z0-9\s]+)\s*-\s*(\d-\d-\d)",
        text
    )

    for med, timing in medicines:

        med = med.strip()

        morning, afternoon, night = timing.split("-")

        if morning == "1":
            reminders.append(
                f"🌅 Morning: Take {med}"
            )

        if afternoon == "1":
            reminders.append(
                f"☀ Afternoon: Take {med}"
            )

        if night == "1":
            reminders.append(
                f"🌙 Night: Take {med}"
            )

    return reminders
