from services.interview_service import generate_question, evaluate_answer

context = """
Skills: Python, Machine Learning
Experience: Data Analyst
"""

# Generate question
question = generate_question(context)

print("\nGenerated Question:\n")
print(question)

# Fake candidate answer
answer = "Polymorphism means many forms."

evaluation = evaluate_answer(question, answer)

print("\nEvaluation:\n")
print(evaluation)