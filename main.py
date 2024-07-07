from typing import Optional, Union, Annotated

from fastapi import Depends, FastAPI
from pydantic import BaseModel

from contextlib import asynccontextmanager
from db import create_table,delete_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    await create_table()
    print('good')
    yield
    print('end')

app = FastAPI(lifespan=lifespan)

class TaskAdd(BaseModel):
    name: str
    description: Optional[str] = None


class Task(TaskAdd):
    id: int

tasks = []

@app.post('/tasks')
async def add_task(task:Annotated[TaskAdd, Depends()]):
    tasks.append(task)
    return {'data': task}


# @app.get("/tasks")
# async def get_tasks():
    # task = Task(name='Cry')
    # return {'data': task}
