import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv() 

# Get API key
api_key=os.getenv("GEMINI_API_KEY")

# Create Gemini client
client=genai.Client(api_key=api_key)

# Send a prompt
res=client.models.generate_content(
    model="gemini-3.5-flash-lite",
    contents="Explain what an LLM is in simple words..."
)

print(res.text)