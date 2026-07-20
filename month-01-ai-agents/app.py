from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()
previous_response_id = None

while True:

    question=input("Ask me anything: ")

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=question,
        previous_response_id=previous_response_id
    )

    previous_response_id = response.id

    print("AI ANSWER: ", response.output_text)