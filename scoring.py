from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def extract_skills(text, taxonomy):
    found = set()
    for category in taxonomy.values():
        for skill in category:
            if skill in text:
                found.add(skill)
    return found

def calculate_ats_score(resume_text, jd_text, taxonomy):

    resume_skills = extract_skills(resume_text, taxonomy)
    jd_skills = extract_skills(jd_text, taxonomy)

    core_skills = set(taxonomy["core"])
    tool_skills = set(taxonomy["tools"])
    process_skills = set(taxonomy["process"])

    # ---- CORE SKILLS (50) ----
    matched_core = resume_skills & core_skills
    core_score = (len(matched_core) / max(len(core_skills), 1)) * 50

    # ---- TOOLS (20) ----
    matched_tools = resume_skills & tool_skills
    tool_score = (len(matched_tools) / max(len(tool_skills), 1)) * 20

    # ---- PROCESS (10) ----
    matched_process = resume_skills & process_skills
    process_score = (len(matched_process) / max(len(process_skills), 1)) * 10

    # ---- EXPERIENCE SIMILARITY (20) ----
    vectorizer = TfidfVectorizer(stop_words="english")
    vectors = vectorizer.fit_transform([resume_text, jd_text])
    similarity = cosine_similarity(vectors[0], vectors[1])[0][0]
    similarity_score = similarity * 20

    final_score = round(core_score + tool_score + process_score + similarity_score)

    missing_skills = list(jd_skills - resume_skills)

    return final_score, missing_skills
