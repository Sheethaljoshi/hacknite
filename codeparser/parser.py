from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import ast

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Set up CORS
origins = [
    "http://localhost",
    "http://localhost:3000",
    "*"
    # Add other origins as needed
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["Authorization", "Content-Type"],
)

class CodeRequest(BaseModel):
    code: str

def parse_python_code(code):
    try:
        # Attempt to parse the code
        ast.parse(code)
        return {"error": False, "message": "Code is valid"}
    except SyntaxError as e:
        # Return the error message
        return {"error": True, "message": str(e)}

@app.post("/checkpythoncode/")
async def check_code(request: CodeRequest):
    code = request.code
    result = parse_python_code(code)
    if result["error"]:
        raise HTTPException(status_code=400, detail=result["message"])
    return result
