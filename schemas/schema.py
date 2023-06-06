from typing import Optional

from pydantic import BaseModel


class QuestionNum(BaseModel):
    questions_num: int
