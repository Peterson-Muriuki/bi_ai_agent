import os
from groq import Groq

# Load API key
api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    print("❌ No API key found in environment.")
    exit()

client = Groq(api_key=api_key)

# Test a simple query
response = client.chat.completions.create(
    model="llama-3.1-8b-instant",  # ✅ updated model
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Say hello from Groq API in one sentence."},
    ]
)

print("✅ Groq API response:")
print(response.choices[0].message.content)  # ✅ fixed
