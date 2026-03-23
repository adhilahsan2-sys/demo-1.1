from fastapi import FastAPI
from backend.routes.resume_routes import router as resume_router
from backend.routes.interview_routes import router as interview_router

app = FastAPI(title="AI Interview Coach API")

app.include_router(resume_router)
app.include_router(interview_router)