import os
from dotenv import load_dotenv
from groq import Groq

# Load .env
load_dotenv()

# Get API key
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("API key not found. Check .env file.")

# Create client
client = Groq(api_key=api_key)

# Test API call
response = client.chat.completions.create(
    model="llama-3.1-8b-instant",
    messages=[
        {"role": "user", "content": "Say hello in one sentence"}
    ]
)

# Print result
print("✅ API Working!")
print(response.choices[0].message.content)