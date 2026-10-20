from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Path,
    Request,
    status
)
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from model import Todo, TodoItem


todo_router = APIRouter()

todo_list = []

templates = Jinja2Templates(directory="templates")


# Добавление новой задачи через HTML-форму
@todo_router.post("/todo", response_class=HTMLResponse)
async def add_todo(
    request: Request,
    todo: Todo = Depends(Todo.as_form)
):
    todo.id = max(
        (task.id for task in todo_list),
        default=0
    ) + 1

    todo_list.append(todo)

    return templates.TemplateResponse(
        request=request,
        name="todo.html",
        context={"todos": todo_list}
    )


# Получение списка всех задач
@todo_router.get("/todo", response_class=HTMLResponse)
async def retrieve_todo(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="todo.html",
        context={"todos": todo_list}
    )


# Просмотр одной задачи
@todo_router.get(
    "/todo/{todo_id}",
    response_class=HTMLResponse
)
async def get_single_todo(
    request: Request,
    todo_id: int = Path(
        ...,
        title="ID задачи"
    )
):
    for todo in todo_list:
        if todo.id == todo_id:
            return templates.TemplateResponse(
                request=request,
                name="todo.html",
                context={"todo": todo}
            )

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="Задача с указанным ID не существует"
    )


# Обновление существующей задачи
@todo_router.put("/todo/{todo_id}")
async def update_todo(
    todo_id: int,
    todo_data: TodoItem
):
    for todo in todo_list:
        if todo.id == todo_id:
            todo.item = todo_data.item

            return {
                "message": "Задача успешно обновлена",
                "todo": todo.model_dump()
            }

    raise HTTPException(
        status_code=404,
        detail="Задача с указанным ID не существует"
    )


# Удаление задачи
@todo_router.delete("/todo/{todo_id}")
async def delete_todo(todo_id: int):
    for index, todo in enumerate(todo_list):
        if todo.id == todo_id:
            todo_list.pop(index)

            return {
                "message": "Задача успешно удалена"
            }

    raise HTTPException(
        status_code=404,
        detail="Невозможно удалить: задача не найдена"
    )
