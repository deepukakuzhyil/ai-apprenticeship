from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

response = client.responses.create(
    model="gpt-4.1-mini",
    input="Explain what a modern LLM-based AI agent is in one sentence."
)

print(response.output_text)