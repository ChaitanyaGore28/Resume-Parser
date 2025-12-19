import PyPDF2
import re
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")
STOP_WORDS = set(stopwords.words("english"))

def extract_text_from_pdf(pdf_file):
    reader = PyPDF2.PdfReader(pdf_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text.lower()

def clean_text(text):
    text = re.sub(r"[^a-zA-Z ]", " ", text)
    words = text.split()
    words = [w for w in words if w not in STOP_WORDS and len(w) > 2]
    return " ".join(words)
