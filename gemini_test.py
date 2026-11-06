from gemini_client import analyze_resume

# Sample resume
resume_text = """
Skills: Python, Java, SQL, HTML
Experience: Python Developer Intern
"""

# Sample job description
job_description = """
Looking for a Python developer with knowledge of
Python, Flask, SQL, REST APIs and Git.
"""

# Call the function
result = analyze_resume(resume_text, job_description)

# Display Gemini's response
print(result)