# 🤖 AI-Powered ATS Resume & Job Matcher

An advanced Natural Language Processing (NLP) web application designed to evaluate resume compatibility against target job descriptions, calculate semantic match scores, and perform automated keyword gap analysis.

🔗 **Live Application:** [ats-resume-matcher-ninad.streamlit.app](https://ats-resume-matcher-ninad.streamlit.app/)

---

## 🚀 Key Features

1. **PDF Text Extraction & Parsing:** Securely extracts raw text layers from uploaded candidate resumes.
2. **Semantic Similarity Scoring:** Utilizes `Scikit-Learn`'s **TF-IDF Vectorization** and **Cosine Similarity** to mathematically compute alignment percentage between documents.
3. **Automated Keyword Gap Analysis:** Identifies critical missing technical skills and action terms present in the job description that are absent from the resume.
4. **Modern Responsive UI:** Features a custom-styled Streamlit interface complete with interactive metrics, professional layout cards, and visual badge tags.

---

## 🛠️ Tech Stack

* **Language:** Python
* **Natural Language Processing (NLP):** Scikit-Learn (TfidfVectorizer, Cosine Similarity), Regex
* **Document Parsing:** PyPDF (pypdf)
* **Frontend / UI:** Streamlit (Custom CSS Layout & Badges)
* **Architecture:** Modular separation of backend NLP pipelines from the frontend user interface

---

## 📂 Project Architecture

```text
ATS-Resume-Matcher/
│
├── backend/
│   └── matcher_backend.py      # PDF text extractor, text cleaner, and TF-IDF similarity engine
├── frontend/
│   └── app.py                  # Main Streamlit dashboard interface with custom CSS styling
├── requirements.txt            # Python package dependencies
└── README.md                   # Project documentation
