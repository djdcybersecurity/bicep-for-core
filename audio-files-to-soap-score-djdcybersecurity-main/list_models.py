import os
from dotenv import load_dotenv
import litellm

load_dotenv()

# Try making a test call to list models (for newer LiteLLM)
try:
    response = litellm.completion(
        model="amazon.nova-lite-v1:0",  # or any model you *think* you're allowed to use
        messages=[{"role": "user", "content": "Hello"}],
        api_key=os.getenv("OPENAI_API_KEY"),
        api_base=os.getenv("OPENAI_BASE_URL"),
    )
    print("Test call successful. You're allowed to use this model.")
except Exception as e:
    print(f"[ERROR] Test call failed:\n{e}")

