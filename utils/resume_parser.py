import fitz

def extract_resume_text(pdf_file):
    doc = fitz.open(pdf_file)
    resume_text = ""
    for page in doc:
        text = page.get_text("text", sort=True)
        if text:
            resume_text += text + "\n"
    doc.close()
    return resume_text.strip()