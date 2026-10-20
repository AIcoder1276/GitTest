from typing import List
from pydantic import BaseModel


class Todo(BaseModel):
    id: int
    item: str


class TodoItem(BaseModel):
    item: str


class TodoItems(BaseModel):
    todos: List[TodoItem]