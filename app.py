from flask import Flask, render_template,request
from utils.resume_parser import extract_resume_text
from gemini_client import analyze_resume

app = Flask(__name__) # Create the Flask application

# HOME ROUTE:
# Handles requests to the homepage ("/")
# Displays the index.html webpage
@app.route("/")  
def home():
    return render_template("index.html")

@app.route("/analyze",methods=["POST"])
def analyze():
    resume_file = request.files["resume"]  # Get the uploaded PDF file

    job_description = request.form["job_description"]  # Get the job description

    pdf_bytes = resume_file.read()  # Read the uploaded PDF as binary data

    resume_text = extract_resume_text(pdf_bytes)   # Extract readable text from the PDF

    result=analyze_resume(resume_file,job_description)

    return render_template(
        "result.html",
        result=result,
        filename=resume_file.filename
    )

if __name__ == "__main__":
    app.run(debug=True)