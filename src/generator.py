from groq import Groq
from config import GROQ_API_KEY, GROQ_MODEL

client = Groq(api_key=GROQ_API_KEY)

def generate_answer(question, chunks):
    context = "\n\n".join(chunks)

    prompt = f"""
You are a helpful assistant.

Answer ONLY using the provided context.

If the answer is not found in the context, say:
"sorry, i wish i could help with that."

Context:
{context}

Question:
{question}
"""

    response = client.chat.completions.create(
        model=GROQ_MODEL,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content