import os

from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi_sqlalchemy import DBSessionMiddleware

from routers import questions

load_dotenv(".env")
app = FastAPI(title="Bewise task", version="0.0.1")
app.add_middleware(DBSessionMiddleware, db_url=os.environ["DATABASE_URL"])
app.include_router(questions.ROUTER)
