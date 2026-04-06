import streamlit as st
from utils import extract_text
from gemini_api import analyze_resume

# ---------------- SESSION STATE ----------------
if "job_role" not in st.session_state:
    st.session_state.job_role = ""

if "job_desc" not in st.session_state:
    st.session_state.job_desc = ""

# ---------------- PAGE ----------------
st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

# ---------------- UI ----------------
st.markdown("""
<style>
.stApp {
    background: linear-gradient(to right, #0f172a, #1e293b);
    color: white;
}
h1 {
    text-align: center;
    color: #38bdf8;
}
.stButton>button {
    background: linear-gradient(90deg, #06b6d4, #3b82f6);
    color: white;
    border-radius: 10px;
    height: 3em;
    font-size: 16px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

st.markdown("<h1>🤖 AI Resume Analyzer</h1>", unsafe_allow_html=True)

# ---------------- INPUT ----------------
col1, col2 = st.columns(2)

with col1:
    uploaded_file = st.file_uploader("📄 Upload Resume", type=["pdf", "docx"])

with col2:
    st.session_state.job_role = st.text_input(
        "🎯 Enter Job Role",
        value=st.session_state.job_role
    )

    st.session_state.job_desc = st.text_area(
        "📋 Or Paste Job Description",
        value=st.session_state.job_desc
    )

    # 🧹 Clear Button
    if st.button("🧹 Clear Input"):
        st.session_state.job_role = ""
        st.session_state.job_desc = ""
        st.rerun()

# ---------------- ANALYZE BUTTON ----------------
if st.button("🚀 Analyze Resume"):

    if not uploaded_file:
        st.error("Please upload a resume ❗")

    elif not st.session_state.job_role and not st.session_state.job_desc:
        st.error("Enter job role or description ❗")

    else:
        st.info("Processing... ⏳")

        resume_text = extract_text(uploaded_file)

        if not resume_text:
            st.error("Failed to extract text ❌")

        else:
            # Decide job input
            if st.session_state.job_desc:
                job_text = st.session_state.job_desc
            else:
                job_text = f"Role: {st.session_state.job_role}"

            try:
                result = analyze_resume(resume_text, job_text)

                st.success("Analysis Complete ✅")

                st.subheader("📊 Result")
                st.text(result)

            except Exception as e:
                st.error(f"Error connecting to AI ❌ {str(e)}")