from fastapi import APIRouter
from crud.questions import get_data
from schemas.schema import QuestionNum

ROUTER = APIRouter(prefix="/questions", tags=["Questions"])


@ROUTER.post('/questions')
def questions(num: QuestionNum):
    questions = get_data(num.questions_num)
    return questions
