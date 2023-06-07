from fastapi import APIRouter
from crud.questions import get_data, all_data_in_db
from schemas.schema import QuestionNum

ROUTER = APIRouter(prefix="/questions", tags=["Questions"])


@ROUTER.post('/questions')
def questions(num: QuestionNum):
    questions = get_data(num.questions_num)
    return questions


@ROUTER.get('/all_data',description='Метод для получения всей информации из БД')
def all_data():
    questions = all_data_in_db()
    return questions
