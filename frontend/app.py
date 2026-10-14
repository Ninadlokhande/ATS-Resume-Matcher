import streamlit as st
import sys
import os

# Add backend directory to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../backend')))
from matcher_backend import extract_text_from_pdf, calculate_match_score

st.set_page_config(
    page_title="AI Resume & Job Description Matcher",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI-Powered ATS Resume & Job Matcher")
st.markdown("Analyze how well your resume matches a target job description, identify missing keywords, and optimize your application score.")
st.markdown("---")

col1, col2 = st.columns(2)

with col1:
    st.subheader("1. Enter Job Description")
    jd_input = st.text_area("Paste the job description here:", height=250, placeholder="Paste requirements, tech stack, and responsibilities...")

with col2:
    st.subheader("2. Upload Your Resume")
    uploaded_file = st.file_uploader("Upload resume (PDF format)", type=["pdf"])
    
    if uploaded_file is not None:
        st.success("Resume uploaded successfully!")

st.markdown("---")

if st.button("🚀 Analyze Match Score", use_container_width=True):
    if not jd_input.strip():
        st.warning("Please paste a job description.")
    elif uploaded_file is None:
        st.warning("Please upload a PDF resume.")
    else:
        with st.spinner("Analyzing semantics and keyword overlap..."):
            resume_text = extract_text_from_pdf(uploaded_file)
            score, missing_skills = calculate_match_score(resume_text, jd_input)
            
        st.subheader("📊 Analysis Results")
        
        # Display score metric with dynamic coloring suggestion
        col_score, col_details = st.columns([1, 2])
        
        with col_score:
            st.metric(label="Overall Match Score", value=f"{score}%")
            if score >= 75:
                st.success("Strong Match! Your resume aligns well with this role.")
            elif score >= 50:
                st.info("Moderate Match. Consider tailoring a few keywords.")
            else:
                st.warning("Low Match. Significant keyword gaps detected.")
                
        with col_details:
            st.markdown("#### 🔍 Recommended Keywords to Add:")
            if missing_skills:
                st.write("Your resume could benefit from incorporating these key terms found in the job description:")
                for skill in missing_skills:
                    st.code(skill, language=None)
            else:
                st.success("Great job! No major critical keyword gaps found.")