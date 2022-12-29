import platform
import os
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:5173",
    "http://127.0.0.2:5173",
    "https://port-5173-osrsdatapluginapi-pancakepuncher802511.codeanyapp.com",
    "https://port-5173-osrsdatapluginapi-pancakepuncher802511.preview.codeanywhere.com"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
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