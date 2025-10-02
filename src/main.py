from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Words(BaseModel):
    words: list[str]

@app.get("/api/v1/me")
def read_me():
    return {"name": "葉富祥", "student_id": "F74146864"}

@app.get("/api/v1/{purpose}")
def calc_area(purpose: str, width: int, height: int):
    area = width * height
    return area

@app.post("/api/v1/word-length-calculator")
def word_length_calculator(words: Words):
    response = []
    for word in words.words:
        response.append({"word": word, "length": len(word)})
    return response
