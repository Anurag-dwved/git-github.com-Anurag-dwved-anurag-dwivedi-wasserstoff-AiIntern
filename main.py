from fastapi import FastAPI
from api import router as api_router

app = FastAPI()

# Include the API router
app.include_router(api_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Document Research & Theme Identification Chatbot!"}

