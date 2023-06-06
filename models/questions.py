from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, Date
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Questions(Base):
    __tablename__ = 'questions'
    id = Column(Integer, primary_key=True, index=False)
    question_text = Column(String)
    answer_text = Column(String)
    date = Column(String)
