import os
from dotenv import load_dotenv
import litellm

load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
BASE_URL = os.getenv("OPENAI_BASE_URL")
MODEL = os.getenv("OPENAI_MODEL", "gpt-3.5-turbo")

def call_soap_llm(transcript: str, case_id: str) -> dict:
    prompt = f"""
You are a medical scribe. Using the transcript below, generate a structured SOAP note in valid JSON format with this structure:

{{
  "case_id": "{case_id}",
  "subjective": "...",
  "objective": "...",
  "assessment": "...",
  "plan": "..."
}}

Transcript:
\"\"\"
{transcript}
\"\"\"

Ensure the JSON is valid and complete.
    """

    response = litellm.completion(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        api_key=API_KEY,
        api_base=BASE_URL
    )

    content = response.choices[0].message["content"]

    # Try to parse JSON block from model output
    try:
        import json
        return json.loads(content)
    except json.JSONDecodeError:
        raise RuntimeError(f"Model returned invalid JSON:\n\n{content}")
