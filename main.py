import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import os
from dotenv import load_dotenv

app = FastAPI()

# Sample
@app.get("/")
def read_root():
    return {"Hello": "World"}

from controller.InternsInfoController import interns_info_router
app.include_router(interns_info_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

    
if __name__ == "__main__":

    # Load environment variables
    load_dotenv(dotenv_path=f"{os.getcwd()}\\envs\\.env")

    uvicorn.run("main:app", host="0.0.0.0", port=int(os.getenv('API_PORT',8000)), reload=True)