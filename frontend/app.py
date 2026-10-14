import streamlit as st
import sys
import os

# Add backend directory to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../backend')))
from matcher_backend import extract_text_from_pdf, calculate_match_score

# Page Configuration
st.set_page_config(
    page_title="AI Resume & Job Matcher Pro",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS Styling for Professional UI
st.markdown("""
    <style>
    .main {
        background-color: #F8FAFC;
    }
    .stButton>button {
        background: linear-gradient(135deg, #0D9488 0%, #0F766E 100%);
        color: white;
        font-weight: 600;
        border-radius: 8px;
        padding: 0.6rem 1.2rem;
        border: none;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        transition: all 0.3s ease;
    }
    .stButton>button:hover {
        background: linear-gradient(135deg, #0F766E 0%, #115E59 100%);
        box-shadow: 0 6px 8px -1px rgba(0, 0, 0, 0.15);
    }
    .metric-card {
        background-color: #FFFFFF;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 1px 3px 0 rgba(0, 0, 0, 0.1);
        border: 1px solid #E2E8F0;
    }
    .skill-badge {
        display: inline-block;
        background-color: #CCFBF1;
        color: #115E59;
        padding: 6px 12px;
        border-radius: 20px;
        font-size: 0.85rem;
        font-weight: 500;
        margin: 4px;
        border: 1px solid #99F6E4;
    }
    </style>
""", unsafe_allow_html=True)

# App Header
st.title("🤖 AI-Powered ATS Resume & Job Matcher")
st.markdown("Optimize your resume against target job descriptions using advanced **TF-IDF Vectorization** and semantic cosine similarity scoring.")
st.markdown("---")

# Main Input Section
col1, col2 = st.columns(2, gap="large")

with col1:
    st.subheader("📋 1. Target Job Description")
    st.markdown("Paste the core requirements, tech stack, and responsibilities.")
    jd_input = st.text_area(
        "Job Description Input",
        height=320,
        placeholder="Paste job description text here...",
        label_visibility="collapsed"
    )

with col2:
    st.subheader("📄 2. Candidate Resume")
    st.markdown("Upload your resume in PDF format for automated parsing.")
    
    # Custom file uploader container styling
    uploaded_file = st.file_uploader(
        "Upload PDF Resume",
        type=["pdf"],
        label_visibility="collapsed"
    )
    
    if uploaded_file is not None:
        st.success(f"✅ File Uploaded: **{uploaded_file.name}**")
    else:
        st.info("💡 Tip: Ensure your resume text layer is selectable for optimal parsing.")

st.markdown("---")

# Analysis Action Button
analyze_btn = st.button("🚀 Run ATS Semantic Analysis", use_container_width=True)

if analyze_btn:
    if not jd_input.strip():
        st.warning("⚠️ Please provide a target job description before running analysis.")
    elif uploaded_file is None:
        st.warning("⚠️ Please upload a candidate resume in PDF format.")
    else:
        with st.spinner("🔄 Extracting text features, cleaning tokens, and calculating cosine similarity..."):
            resume_text = extract_text_from_pdf(uploaded_file)
            score, missing_skills = calculate_match_score(resume_text, jd_input)
            
        st.markdown("## 📊 Executive Analysis Results")
        
        # Results Layout
        res_col1, res_col2 = st.columns([1.2, 2], gap="large")
        
        with res_col1:
            st.markdown("### Match Score Evaluation")
            st.metric(label="Overall Semantic Match", value=f"{score}%")
            
            if score >= 75:
                st.success("🌟 **Strong Match!** Your profile aligns exceptionally well with the core job requirements.")
            elif score >= 50:
                st.info("📈 **Moderate Match.** Good baseline alignment, but targeted keyword optimization can significantly boost your rank.")
            else:
                st.warning("⚠️ **Low Match.** Major keyword gaps detected between your resume and the target description.")

        with res_col2:
            st.markdown("### 🔍 Recommended Keyword Additions")
            st.markdown("Incorporating these missing terms from the job description can improve parser ranking:")
            
            if missing_skills:
                badges_html = "".join([f'<span class="skill-badge">📌 {skill}</span>' for skill in missing_skills])
                st.markdown(f'<div style="padding: 10px 0;">{badges_html}</div>', unsafe_allow_html=True)
            else:
                st.success("🎉 Excellent! No critical keyword discrepancies identified.")

# Sidebar Information Guide
with st.sidebar:
    st.image("https://img.icons8.com/color/96/resume.png", width=80)
    st.subheader("About the Engine")
    st.write("This tool evaluates text compatibility by converting raw text documents into high-dimensional TF-IDF vectors and computing mathematical cosine distance.")
    
    st.markdown("---")
    st.markdown("### 🚀 Core Capabilities")
    st.markdown("""
    * **PDF Text Extraction:** Parses clean raw text from structured documents.
    * **Semantic Tokenization:** Filters stop-words and isolates technical terms.
    * **Gap Analysis:** Identifies high-priority missing skills for resume tailoring.
    """)
    st.markdown("---")
    st.caption("Designed for Professional Analytics Portfolios")