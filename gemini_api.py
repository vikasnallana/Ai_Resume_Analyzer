from google.genai import Client
from dotenv import load_dotenv
import os

# Load env
load_dotenv()

# Initialize client
client = Client(api_key=os.getenv("GEMINI_API_KEY"))


def analyze_resume(resume_text, job_text):
    try:
        prompt = f"""
You are an AI Resume Analyzer.

Analyze the following resume against the given job requirement.

Resume:
{resume_text}

Job Requirement:
{job_text}

Give output in this format:

1. Match Percentage: 

2. Matching Skills:
- skill 1
- skill 2

3. Missing Skills:
- skill 1
- skill 2

4. Strengths:
- point 1
- point 2

5. Improvements:
- point 1
- point 2

6. Ats Score : 

7. Final Feedback:
(short summary)

And remeber that you should respond like a teacher and ai analyzer only give the short answers or response dont include long text 
"""

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:
        return f"ERROR: {str(e)}"