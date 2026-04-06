from backend.utils.file_loader import extract_text_from_pdf
from backend.utils.text_chunker import chunk_text
from backend.rag.vector_store import store_resume_chunks
from backend.llm.groq_client import ask_groq
from backend.utils.logger import log_event


# ✅ RESUME SUMMARY (unchanged)
def summarize_resume(text):

    prompt = f"""
You are an AI career assistant.

Summarize the following resume into 4–5 bullet points highlighting:

- Skills
- Experience
- Education
- Key strengths

Resume:
{text}
"""

    return ask_groq(prompt)


# ✅ NEW: SKILL EXTRACTION WITH EXPLANATION
def extract_skills_with_explanation(text, session_id="default"):

    prompt = f"""
You are an AI resume analyzer.

From the resume below:

{text}

Extract EXACTLY 3–5 key skills.

For EACH skill:
- Provide the skill name
- Provide a clear reason with evidence from the resume

STRICT RULES:
- DO NOT summarize the resume
- DO NOT give general statements like "good communication"
- Each reason MUST reference something specific (project, tool, role)
- If no evidence exists, DO NOT include that skill

OUTPUT FORMAT (STRICT):

Skill: Python
Reason: Used in machine learning project mentioned in resume

Skill: Leadership
Reason: Led hackathon and managed team activities

ONLY return skills in this format. No extra text.
"""

    result = ask_groq(prompt).strip()

    # 🔥 PRINT FOR BACKEND
    print("\n===== SKILL EXPLANATION =====")
    print(result)

    # 🔥 LOG
    log_event("SKILL_EXPLANATION", result, session_id)

    return result


# ✅ MAIN PROCESS FUNCTION
def process_resume(file_path, session_id="default"):

    print("Processing resume...")

    # Step 1: Extract text
    text = extract_text_from_pdf(file_path)

    # Step 2: Chunk text
    chunks = chunk_text(text)

    # Step 3: Store embeddings
    store_resume_chunks(chunks)

    # Step 4: Generate summary
    summary = summarize_resume(text)

    # Step 5: Extract skills with explanation (NEW 🔥)
    skills = extract_skills_with_explanation(text, session_id)

    print("Resume processed successfully!")

    return {
        "chunks": chunks,
        "summary": summary,
        "skills": skills   # ✅ NEW OUTPUT
    }