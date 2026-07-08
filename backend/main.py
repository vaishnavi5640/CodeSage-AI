from fastapi import FastAPI
from app.routes.review import router as review_router
from app.routes.upload import router as upload_router

app = FastAPI(title="CodeSage AI")

app.include_router(review_router)
app.include_router(upload_router)

@app.get("/")
def home():
    return {"message": "Welcome to CodeSage AI 🚀"}