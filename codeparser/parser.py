from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import ast

app = FastAPI()

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
