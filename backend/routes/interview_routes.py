from fastapi import APIRouter
from pydantic import BaseModel
from backend.services.interview_service import generate_question, evaluate_answer
from backend.utils.logger import log_event   # ✅ NEW

router = APIRouter()


class QuestionRequest(BaseModel):
    context: str


class AnswerRequest(BaseModel):
    question: str
    answer: str


@router.post("/generate-question")
def generate_question_api(request: QuestionRequest):

    question = generate_question(request.context)

    return {
        "question": question
    }


@router.post("/evaluate-answer")
def evaluate_answer_api(request: AnswerRequest):

    # 🔥 LOG USER ANSWER (FIX)
    log_event("USER_ANSWER", request.answer)

    evaluation = evaluate_answer(request.question, request.answer)

    return {
        "evaluation": evaluation
    }