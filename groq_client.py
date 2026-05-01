import os
import time
import logging
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

# Setup logging
logging.basicConfig(
    filename="groq_errors.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class GroqClient:
    def __init__(self):
        api_key = os.getenv("GROQ_API_KEY")
        if not api_key:
            raise ValueError("API key not found in .env file")

        self.client = Groq(api_key=api_key)

    def generate(self, prompt, retries=3):
        delay = 1  # seconds

        for attempt in range(retries):
            try:
                response = self.client.chat.completions.create(
                    model="llama-3.1-8b-instant",
                    messages=[{"role": "user", "content": prompt}]
                )

                # JSON parsing (safe)
                content = response.choices[0].message.content

                return {
                    "success": True,
                    "data": content
                }

            except Exception as e:
                logging.error(f"Attempt {attempt+1} failed: {str(e)}")

                if attempt == retries - 1:
                    return {
                        "success": False,
                        "error": str(e)
                    }

                # Exponential backoff
                time.sleep(delay)
                delay *= 2   # 1 → 2 → 4