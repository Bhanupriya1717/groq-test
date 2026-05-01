from groq_client import GroqClient

client = GroqClient()

result = client.generate("Explain Artificial Intelligence in one sentence")

if result["success"]:
    print("✅ Response:", result["data"])
else:
    print("❌ Error:", result["error"])