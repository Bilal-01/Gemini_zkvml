import uvicorn
from fastapi import FastAPI, Request, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import sys

try:
    sys.path.append('./app')
    
    from service import generatePrompt
except Exception as e:
    print(e)


class PromptInputs(BaseModel):
    inputCode: str
    
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/")
def getPrompt(req: PromptInputs):
    response = generatePrompt(req.inputCode)
    return {
        "response": response
    }
    
if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=80)