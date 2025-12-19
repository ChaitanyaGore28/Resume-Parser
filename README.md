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

