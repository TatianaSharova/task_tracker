from fastapi import FastAPI

from contextlib import asynccontextmanager
from backend.db import create_table,delete_tables
from backend.routers import router as t_router


@asynccontextmanager
async def lifespan(app: FastAPI):
    await delete_tables()
    await create_table()
    print('good')
    yield
    print('end')

app = FastAPI(lifespan=lifespan)

app.include_router(t_router)