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

    print("Resume text received by Gemini:", resume_text)
    
    prompt = f"""
    You are an expert resume reviewer.

    Analyse the following resume against the job description.

    RESUME:
    {resume_text}

    JOB DESCRIPTION:
    {job_description}

    Present your analysis using exactly these four sections:

    1. OVERALL MATCH SCORE
    Give a score out of 100 and briefly explain the score.

    2. MATCHING SKILLS
    List the skills from the resume that match the job description.

    3. MISSING SKILLS
    List important skills required by the job description
    that are not found in the resume.

    4. IMPROVEMENT SUGGESTIONS
    Give practical suggestions to improve the resume
    for this particular job.

    Important rules:
    - Do not invent qualifications or experience.
    - Only consider information actually present in the resume.
    - If information is unavailable, clearly mention that.
    - Be honest and specific in your evaluation.
    """


    # Send a prompt
    response=client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents=prompt
    )

    return response.text

