# =========================================
# FILE: app.py
# =========================================

import streamlit as st

from utils.pdf_extractor import extract_text_from_pdf
from utils.image_extractor import extract_text_from_image
from utils.medical_analyzer import analyze_report
from utils.medicine_analyzer import analyze_medicines
from utils.health_score import calculate_health_score
from utils.symptom_analyzer import analyze_symptoms

# ---------------- PAGE CONFIG ---------------- #

st.set_page_config(
    page_title="MediMind AI Pro+",
    page_icon="🩺",
    layout="wide"
)

# ---------------- HEADER ---------------- #

st.title("🩺 MediMind AI Pro+")
st.subheader("AI-Powered Healthcare Assistant")

# ---------------- SIDEBAR ---------------- #

st.sidebar.title("🩺 MediMind AI")

st.sidebar.info(
    """
    Features:

    ✅ PDF Analysis
    ✅ Screenshot Analysis
    ✅ Mobile Camera Scan
    ✅ OCR Text Detection
    ✅ Medical Report Analysis
    ✅ Prescription Intelligence
    ✅ Symptom Detection
    ✅ Emergency Alerts
    ✅ Health Score Detection
    """
)

# ---------------- FILE UPLOAD ---------------- #

uploaded_file = st.file_uploader(
    "📤 Upload Medical Report",
    type=["pdf", "png", "jpg", "jpeg"]
)

# ---------------- CAMERA INPUT ---------------- #

camera_image = st.camera_input(
    "📸 Take a Photo of Medical Report"
)

# ---------------- MAIN APP ---------------- #

if uploaded_file or camera_image:

    st.success("✅ File Received Successfully!")

    # ---------------- FILE PROCESSING ---------------- #

    if uploaded_file:

        file_type = uploaded_file.name.split(".")[-1].lower()

        # PDF Processing
        if file_type == "pdf":

            extracted_text = extract_text_from_pdf(uploaded_file)

        # Image Processing
        else:

            extracted_text = extract_text_from_image(uploaded_file)

    # Camera Image Processing
    elif camera_image:

        extracted_text = extract_text_from_image(camera_image)

    # ---------------- SHOW EXTRACTED TEXT ---------------- #

    st.subheader("📄 Extracted Medical Report")

    st.text_area(
        "Detected Text",
        extracted_text,
        height=300
    )

    # ---------------- AI HEALTH ANALYSIS ---------------- #

    st.subheader("🧠 AI Health Analysis")

    analysis = analyze_report(extracted_text)

    if analysis:

        for item in analysis:

            if "⚠" in item:
                st.error(item)

            else:
                st.success(item)

    else:

        st.info("No medical parameters detected.")

    # ---------------- HEALTH SCORE ---------------- #

    st.subheader("💚 Health Score")

    health_score = calculate_health_score(analysis)

    st.progress(health_score)

    st.write(f"### Health Score: {health_score}/100")

    # ---------------- PRESCRIPTION INTELLIGENCE ---------------- #

    st.subheader("💊 Prescription Intelligence")

    medicine_analysis = analyze_medicines(extracted_text)

    if medicine_analysis:

        for med in medicine_analysis:

            if "🚨" in med:
                st.error(med)

            elif "⚠" in med:
                st.warning(med)

            else:
                st.success(med)

    else:

        st.info("No medicines detected.")

    # ---------------- SYMPTOM DETECTION ---------------- #

    st.subheader("🧠 Symptom Detection")

    symptom_analysis = analyze_symptoms(extracted_text)

    if symptom_analysis:

        for symptom in symptom_analysis:

            if "🚨" in symptom:
                st.error(symptom)

            elif "⚠" in symptom:
                st.warning(symptom)

            else:
                st.success(symptom)

    else:

        st.info("No symptoms detected.")

else:

    st.info("📤 Upload a medical report or scan using camera.")