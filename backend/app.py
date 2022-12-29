import platform
import os
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv_vault import load_dotenv

load_dotenv(".env")

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("ORIGINS").split(","),
    allow_credentials=True,
    allow_methods=["GET", "POST", "HEAD", "OPTIONS"],
    allow_headers=["Content-Type","Set-Cookie"],
)

@app.get("/")
async def root():

    return "Main Route/Endpoint Placeholder!"

if __name__ == "__main__":

    if platform.system() == "Windows":
        ip = "127.0.0.1"
    elif platform.system() == "Linux":
        ip = "0.0.0.0"
        
    uvicorn.run("app:app",
            host=ip,
            port=8000,
            reload=True,
            )