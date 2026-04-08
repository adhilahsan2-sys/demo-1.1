import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = None


def _get_client():
    global client

    if client is not None:
        return client

    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError(
            "GROQ_API_KEY is not set. Add it to your environment or pass it to Docker with -e GROQ_API_KEY=..."
        )

    client = Groq(api_key=api_key)
    return client


def ask_groq(prompt):
    groq_client = _get_client()

    response = groq_client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    return response.choices[0].message.content