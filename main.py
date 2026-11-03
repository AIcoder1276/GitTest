from fastapi import FastAPI

from routes.users import user_router
from routes.events import event_router

import uvicorn


app = FastAPI(
    title="Пашин Илья — Практическая работа №7",
    description="Структурирование приложений FastAPI. "
                "Планировщик событий.",
    version="1.0.0"
)


# Подключение пользовательских маршрутов
app.include_router(
    user_router,
    prefix="/user"
)


# Подключение маршрутов событий
app.include_router(
    event_router,
    prefix="/event"
)


@app.get("/", tags=["Главная"])
async def home():
    return {
        "application": "Event Planner",
        "author": "Пашин Илья",
        "practical_work": 7,
        "message": "Приложение успешно работает"
    }


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="127.0.0.1",
        port=8080,
        reload=True
    )
