from fastapi import FastAPI
from routes.resume_routes import router as resume_router
from routes.interview_routes import router as interview_router

app = FastAPI(title="AI Interview Coach API")

app.include_router(resume_router)
app.include_router(interview_router)