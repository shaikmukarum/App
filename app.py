import streamlit as st

# --- Page config ---
st.set_page_config(page_title="TeleHealth Demo", page_icon="🩺", layout="centered")

st.title("🩺 TeleHealth – AI Symptom Checker")
st.write(
    "Prototype web app for Smart India Hackathon 2025\n\n"
    "⚠️ This is a **demo only** – not for real medical use."
)

# --- Symptom input ---
symptoms = st.text_area("Describe your symptoms (you can use any language):", height=100)

# --- Demo triage logic ---
def analyze(sym):
    text = sym.lower()
    if any(x in text for x in ["fever", "cough", "cold"]):
        return "Flu / Viral fever", "Basic"
    if any(x in text for x in ["chest pain", "difficulty breathing", "severe"]):
        return "Possible cardiac / respiratory issue", "Critical"
    if any(x in text for x in ["headache", "blurred vision"]):
        return "Migraine or vision problem", "Basic"
    return "Condition unclear – consult a doctor", "Basic"

if st.button("Analyze my symptoms"):
    if symptoms.strip() == "":
        st.warning("Please type something first.")
    else:
        diagnosis, level = analyze(symptoms)
        st.subheader("🔍 Possible Diagnosis")
        st.info(diagnosis)

        st.subheader("📌 Urgency Level")
        if level == "Critical":
            st.error("🚨 Critical – see a doctor immediately!")
            st.markdown(
                "[💬 Start Video Consultation](https://meet.jit.si/TeleHealthDemo)",
                unsafe_allow_html=True
            )
        else:
            st.success("Basic – self care or visit a clinic if needed.")

st.caption("Made with Streamlit · Team Smart · SIH 2025")
