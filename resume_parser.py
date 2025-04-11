# backend/services/resume_parser.py

import fitz  # PyMuPDF

def extract_text_from_pdf(file_path: str) -> str:
    try:
        text = ""
        with fitz.open(file_path) as doc:
            for page in doc:
                text += page.get_text()
        return text
    except Exception as e:
        return f"Error extracting text from resume: {str(e)}"
