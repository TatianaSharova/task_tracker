from typing import Annotated
from fastapi import Depends
from fastapi import APIRouter
from orm_query import TaskRepository

from schemas import TaskAdd

router = APIRouter(
   prefix="/tasks",
   tags=["задачи"],
)


@router.post('')
async def add_task(task:Annotated[TaskAdd, Depends()]):
    task_id = await TaskRepository.add_task(task)
    return {'data': task, 'task_id': task_id}


@router.get('')
async def get_tasks():
    tasks = await TaskRepository.get_all()
    return {'data': tasks}