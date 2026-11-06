from flask import Flask, render_template,request
from utils.resume_parser import extract_resume_text

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

    # Display the extracted resume text
    return f"""
    <h2>Resume Text Extracted Successfully!</h2>

    <h3>Uploaded Resume:</h3>
    <p>{resume_file.filename}</p>

    <h3>Extracted Resume Content:</h3>
    <pre>{resume_text}</pre>
    """

if __name__ == "__main__":
    app.run(debug=True)