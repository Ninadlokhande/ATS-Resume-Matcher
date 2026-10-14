import pypdf
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import re

def extract_text_from_pdf(uploaded_file):
    """Extracts raw text from an uploaded PDF file."""
    reader = pypdf.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        extracted = page.extract_text()
        if extracted:
            text += extracted + "\n"
    return text

def clean_text(text):
    """Basic text cleaning: lowercase and remove special characters."""
    text = text.lower()
    text = re.sub(r'[^a-z0-9\s]', '', text)
    return text

def calculate_match_score(resume_text, job_description):
    """Calculates cosine similarity percentage between resume and job description."""
    if not resume_text.strip() or not job_description.strip():
        return 0.0, []
    
    cleaned_resume = clean_text(resume_text)
    cleaned_jd = clean_text(job_description)
    
    # Vectorize texts using TF-IDF
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform([cleaned_resume, cleaned_jd])
    
    # Calculate similarity score (0 to 1 -> convert to percentage)
    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    match_percentage = round(similarity * 100, 2)
    
    # Keyword Gap Analysis
    feature_names = vectorizer.get_feature_names_out()
    resume_vector = tfidf_matrix.toarray()[0]
    jd_vector = tfidf_matrix.toarray()[1]
    
    # Identify key terms present in JD but weak/missing in resume
    missing_keywords = []
    for i, word in enumerate(feature_names):
        if jd_vector[i] > 0.05 and resume_vector[i] == 0:
            missing_keywords.append(word)
            
    return match_percentage, missing_keywords[:10] # Return top 10 missing skills