# ATS Resume Scorer

## Overview

This project implements a simplified **Applicant Tracking System (ATS)** that evaluates how well a resume matches a given job description.

The objective is to simulate **early-stage resume screening** by focusing on:
- Skill relevance  
- Tooling exposure  
- Role alignment  

rather than relying on generic text similarity.

The system compares **one resume against one job description** and produces:
- An ATS-style match score
- Identified missing or weak skills
- Practical improvement suggestions

This project is designed as a **transparent and explainable screening tool**, not as a predictive hiring model.

---

## Key Features

- Resume parsing from PDF format  
- Job description analysis  
- Automatic job domain detection  
- Domain-specific skill evaluation  
- Weighted and explainable ATS scoring  
- Clear identification of missing skills  
- Simple Streamlit-based user interface  

---

## Tech Stack

- **Language:** Python  
- **UI:** Streamlit  
- **NLP:** TF-IDF + rule-based skill matching  

### Libraries Used
- scikit-learn  
- PyPDF2  
- NLTK  

---

## How the System Works

### 1. Input
- User uploads a resume in PDF format  
- User pastes a job description  

### 2. Domain Detection
The job description is analyzed to determine the most relevant job domain  
(e.g., Android, Full Stack, Backend, ML, DevOps).

This ensures the resume is evaluated **only against relevant expectations**.

### 3. Skill Extraction
Instead of treating every word as a skill, the system validates job requirements against **curated domain-specific skill taxonomies**.

This prevents filler or descriptive language from influencing the score.

### 4. Scoring Logic
The ATS score is computed using a weighted approach:

- Core technical skills – **50%**
- Tools & technologies – **20%**
- Development practices & processes – **10%**
- Resume–JD experience similarity – **20%**

This approach keeps the scoring **stable, fair, and explainable**.

### 5. Output
- ATS match score (0–100)  
- Detected job domain  
- Missing or weak skills  
- Improvement suggestions  

---

## Project Structure
```
ATS_Resume_Scorer/
│
├── app.py # Streamlit UI
├── scoring.py # ATS scoring logic
├── domain_detection.py # Job domain detection
├── skills.py # Domain-specific skill sets
├── utils.py # PDF parsing & text cleaning
└── README.md
```

---

## How to Run the Project

### 1. Install dependencies
```bash
pip install stramlit
pip install nltk
pip install scikit-learn
pip install PyPDF2
streamlit run app.py
```
##  Access the app

Open your browser and visit:
👉 http://localhost:8501
---
## Limitations

This system does not use supervised learning or any labeled resume datasets, so standard accuracy metrics are not calculated.

The skill lists are manually curated for common domains and may not include very niche or newly emerging technologies.

Experience level and leadership requirements are identified using simple rules and may not fully capture senior-level expectations.

The suggestions provided are rule-based and do not use large language models for detailed or personalized recommendations.

---
