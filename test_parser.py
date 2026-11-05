from utils.resume_parser import extract_resume_text

pdf_file = "sample_resume.pdf"
text = extract_resume_text(pdf_file)
print(text)