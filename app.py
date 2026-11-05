from flask import Flask, render_template,request

app = Flask(__name__) # Create the Flask application

# HOME ROUTE:
# Handles requests to the homepage ("/")
# Displays the index.html webpage
@app.route("/")  
def home():
    return render_template("index.html")

@app.route("/analyze",methods=["POST"])
def analyze():
    resume_file=request.files["resume"]
    job_description=request.form["job_description"]
    return f"""
    <h2>Successfully received your information!</h2>
    <p>Resume: {resume_file.filename}</p>
    <p>Job Description: {job_description}</p>
    """

if __name__ == "__main__":
    app.run(debug=True)