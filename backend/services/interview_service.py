from backend.llm.groq_client import ask_groq


def generate_question(context):

    prompt = f"""
You are a technical interviewer.

Based on the candidate resume:

{context}

Generate ONE short technical interview question.
The question should be concise and suitable for a live interview.
Do not include explanations or evaluation criteria.
"""

    return ask_groq(prompt)


def evaluate_answer(question, answer):

    prompt = f"""
You are an AI interview evaluator.

Question:
{question}

Candidate Answer:
{answer}

Evaluate the answer and return:

Score (0-10)
Strengths
Improvements
"""

    return ask_groq(prompt)