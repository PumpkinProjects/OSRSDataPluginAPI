import platform
import os
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv_vault import load_dotenv
from routes.plugin_init import init_route
from routes.data_routes import recieve

# Loads a .env file for enviroment variables.
load_dotenv(".env")

# Instantiates an object named app of type FastAPI(). This is an essential object for FastAPI to work.
app = FastAPI()

# Specifies that the FastAPI will be using a middleware. Default is CORS.
app.add_middleware(
    CORSMiddleware,
    allow_origins=os.getenv("ORIGINS").split(","),
    allow_credentials=True,
    allow_methods=["GET", "POST", "HEAD", "OPTIONS"],
    allow_headers=["Content-Type","Set-Cookie"],
)

app.include_router(init_route.router)
app.include_router(recieve.router)

# This is a basic route to capture API traffic on the "/" or root endpoint.
# Currently defaulted for testing purposes.
@app.get("/")
async def root():

    return "Main Route/Endpoint Placeholder!"

# This if statement is the entry point for the application.
# I add this to all my application entry point files.
# It's not entirely necesssary, but it's an easy and safe way to execute special code when this script runs.
# It also just serves as an indicator of where the script starts.
if __name__ == "__main__":

    # Checks what Operating System you are on to determine which localhost to use for hosting.
    # This is primarily for the devolopment build when working between windows or linux.
    if platform.system() == "Linux":
        ip = "0.0.0.0"
    else:
        ip = "127.0.0.1"
    
    # Runs FastAPI App using Uvicorn ASGI on the specified localhost, port, and allows the application to reload in realtime when code changes.
    uvicorn.run("app:app",
            host=ip,
            port=8000,
            reload=True,
            )