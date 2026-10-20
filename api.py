from fastapi import FastAPI 
from todo import todo_router
from model import Todo 
app = FastAPI(    title="Пашин Илья — Практическая работа №6",
    description="Шаблоны Jinja2 в FastAPI. Приложение Todo.",
    version="1.0.0")

@app.get("/")
async def welcome() -> dict:
	return { "message": "Hello World"}
app.include_router(todo_router) 
