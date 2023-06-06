from fastapi_sqlalchemy import db
import requests
from models.questions import Questions as QuestionModel


def get_data(q_count):
    counter = 0

    while counter < q_count:
        question = requests.get(url=f'https://jservice.io/api/random?count=1')
        if question.status_code != 200:
            print('ERR', counter)
            continue
        qstn = db.session.query(QuestionModel).filter(QuestionModel.id == question.json()[0]['id']).first()
        if qstn:
            print('SKIPPED')
            continue
        question = question.json()[0]
        q_id = question['id']
        q_answer = question['answer']
        q_question = question['question']
        q_date = question['created_at']
        questions_schema = QuestionModel(id=q_id, question_text=q_question, answer_text=q_answer, date=q_date)
        db.session.add(questions_schema)
        db.session.commit()
        counter += 1
        print(counter, question['id'])
    return db.session.query(QuestionModel).all()
