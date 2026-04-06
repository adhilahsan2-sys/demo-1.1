from backend.llm.groq_client import ask_groq
from backend.utils.logger import log_event


# ✅ SKILL EXTRACTION WITH EXPLANATION (NEW)
def extract_skills_with_explanation(context, session_id="default"):

    prompt = f"""
From the following resume:

{context}

Extract key skills and explain WHY each skill is selected.

Return in this format:

Skill: <skill name>
Reason: <why selected from resume>
"""

    result = ask_groq(prompt)

    # 🔥 LOG SKILL EXPLANATION
    log_event("SKILL_EXPLANATION", result, session_id)

    return result


# ✅ QUESTION GENERATION
def generate_question(context, session_id="default"):

    prompt = f"""
You are a strict technical interviewer.

Based ONLY on the candidate resume:

{context}

Generate ONE short technical interview question.

Rules:
- No explanation
- No hallucination
- Only use given context
"""

    # Generate question
    question = ask_groq(prompt)

    # 🔥 LOG INPUT CONTEXT
    log_event("QUESTION_CONTEXT", str(context)[:300], session_id)

    # 🔥 LOG GENERATED QUESTION
    log_event("GENERATED_QUESTION", question, session_id)

    return question


# ✅ EVALUATION WITH EXPLAINABLE SCORING
def evaluate_answer(question, answer, session_id="default"):

    prompt = f"""
You are an AI interview evaluator.

Question:
{question}

Candidate Answer:
{answer}

Evaluate the answer using this rubric:

1. Relevance (0-3)
2. Clarity (0-2)
3. Technical Depth (0-3)
4. Structure (0-2)

Return STRICTLY in this format:

Relevance: X/3
Clarity: X/2
Technical Depth: X/3
Structure: X/2

Final Score: X/10

Strengths:
- ...

Improvements:
- ...
"""

    # Generate evaluation
    result = ask_groq(prompt)

    # 🔥 LOG INPUT (QUESTION + ANSWER)
    log_event(
        "EVALUATION_INPUT",
        {
            "question": question,
            "answer": answer
        },
        session_id
    )

    # 🔥 LOG OUTPUT (RESULT)
    log_event("EVALUATION_RESULT", result, session_id)

    return result