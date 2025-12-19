import streamlit as st

from utils import extract_text_from_pdf, clean_text
from domain_detection import detect_domain
from skills import SKILLS
from scoring import calculate_ats_score

st.set_page_config(
    page_title="ATS Resume Scorer",
    layout="centered"
)

st.title("ATS Resume Scorer")
st.write(
    "Upload your resume and paste the job description to get an ATS-style compatibility score."
)

#User inputs
resume_file = st.file_uploader("Upload Resume (PDF)", type=["pdf"])
job_description = st.text_area("Paste Job Description")

#Analysis
if st.button("Analyze Resume"):
    if resume_file is None or job_description.strip() == "":
        st.error("Please upload a resume and provide a job description.")
    else:
        # 1. Extract & clean text
        resume_text = clean_text(extract_text_from_pdf(resume_file))
        jd_text = clean_text(job_description)

        # 2. Detect domain
        domain = detect_domain(jd_text)

        # 3. Load domain-specific taxonomy
        taxonomy = SKILLS[domain]

        # 4. Calculate ATS score
        score, missing_skills = calculate_ats_score(
            resume_text,
            jd_text,
            taxonomy
        )

        #Output
        st.subheader("ATS Score")
        st.metric("Resume Match Score", f"{score} / 100")

        st.subheader("Detected Job Domain")
        st.write(domain.capitalize())

        st.subheader("Missing Skills / Keywords")
        if missing_skills:
            st.write(", ".join(sorted(missing_skills)))
        else:
            st.write("No major required skills missing.")

        st.subheader("Strengths")
        st.write(
            "Your resume demonstrates relevant experience and technical exposure aligned with the job domain."
        )

        st.subheader("Suggestions")
        st.write(
            "Consider adding the missing skills naturally in your project descriptions or technical skills section."
        )
