from fastapi import FastAPI
from app.api.view import router

app = FastAPI(title="Welcome to the Celery app.")

app.include_router(router)