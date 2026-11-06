import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv("GEMINI_API_KEY")

# Create Gemini client
client = genai.Client(api_key=api_key)

def analyze_resume(resume_text,job_description):
    prompt=f"""
    You are an expert resume reviewer.

    Analyse the following resume against the job description.

    RESUME:
    {resume_text}

    JOB DESCRIPTION:
    {job_description}

    Provide:
    1. Overall match score out of 100.
    2. Matching skills.
    3. Missing skills.
    4. Suggestions to improve the resume.

    Do not invent any qualifications or experience.
    """

    # Send a prompt
    response=client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=prompt
    )

    return response.text

