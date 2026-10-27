
import os
from dotenv import load_dotenv
from groq import Groq

# Load the .env file from the current folder
load_dotenv()

# Read the API key
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError(
        "API key not found. Check your .env file and variable name."
    )

client = Groq(api_key=my_api_key)

model = "openai/gpt-oss-120b"

messages = [
    {
        "role": "user",
        "content": "Do you know Padho with Pratyush?"
    }
]

response = client.chat.completions.create(
    model=model,
    messages=messages
)

print(response.choices[0].message.content)
