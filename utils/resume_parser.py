import fitz

def extract_resume_text(pdf_bytes):
    doc = fitz.open(stream=pdf_bytes,filetype="pdf")
    resume_text = ""
    for page in doc:
        text = page.get_text("text", sort=True)
        if text:
            resume_text += text + "\n"
    doc.close()
    return resume_text.strip()