def detect_domain(jd_text):
    jd_text = jd_text.lower()

    if any(k in jd_text for k in ["android", "kotlin", "apk"]):
        return "android"
    if any(k in jd_text for k in ["react", "node", "frontend", "full stack"]):
        return "fullstack"
    if any(k in jd_text for k in ["spring", "fastapi", "backend"]):
        return "backend"
    if any(k in jd_text for k in ["machine learning", "data science", "pandas"]):
        return "ml"
    if any(k in jd_text for k in ["devops", "docker", "ci/cd", "aws"]):
        return "devops"

    return "backend"  # safe default
