from fastapi import FastAPI, APIRouter
from pydantic import BaseModel

app = FastAPI()
router = APIRouter(prefix="/api/v1")

class Words(BaseModel):
    words: list[str]

@router.get("/me")
def read_me():
    return {"name": "葉富祥", "student_id": "F74146864"}

@router.get("/rectangle-area")
def calc_area(width: int, height: int):
    area = width * height
    return area

@router.post("/word-length-calculator")
def word_length_calculator(words: Words):
    response = []
    for word in words.words:
        response.append({"word": word, "length": len(word)})
    return response

app.include_router(router)