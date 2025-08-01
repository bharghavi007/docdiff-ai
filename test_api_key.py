import openai
from dotenv import load_dotenv
import os

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

try:
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Hello, this is a test."}],
        max_tokens=10
    )
    print("API Key is valid! Response:", response.choices[0].message.content)
except Exception as e:
    print("Error:", str(e))