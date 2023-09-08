from fastapi import FastAPI, Depends, HTTPException

app = FastAPI()

API_KEY = "secret-api-key"

def verify_api_key(api_key: str = Depends()):
    if api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")
    return api_key
# Dependency: Check if the number is positive
def is_positive_number(number: int):
    if number <= 0:
        raise HTTPException(status_code=400, detail="Number must be positive")
    return number

# API route that uses the dependency
@app.get("/square/")
async def calculate_square(number: int = Depends([is_positive_number, verify_api_key])):
    square = number * number
    return {"number": number, "square": square}
