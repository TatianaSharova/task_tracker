from sqlalchemy import select
from db import db_session, TaskDB
from schemas import TaskAdd, Task


class TaskRepository:
   '''Так как работа с одной таблицей, возьмем методы в класс.'''
   @classmethod
   async def add_task(cls, task: TaskAdd) -> int:
       async with db_session() as session:
           data = task.model_dump()
           new_task = TaskDB(**data)
           session.add(new_task)
           await session.flush()
           await session.commit()
           return new_task.id

   @classmethod
   async def get_all(cls) -> list[Task]:
       async with db_session() as session:
           query = select(TaskDB)
           result = await session.execute(query)
           task_models = result.scalars().all()
           tasks = [Task.model_validate(task_model) for task_model in task_models]
           return tasks
