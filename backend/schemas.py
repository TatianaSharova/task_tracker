from typing import Optional

from pydantic import BaseModel, ConfigDict


class TaskAdd(BaseModel):
    name: str
    description: Optional[str] = None


class Task(TaskAdd):
    id: int
    model_config = ConfigDict(from_attributes=True)
