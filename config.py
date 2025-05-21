import os

class Config:
    GROQ_API_KEY = os.getenv("GROQ_API_KEY")  # Set your Groq API key as an environment variable
    DATABASE_URL = os.getenv("DATABASE_URL")  # Database connection string
 
