from fastapi import FastAPI

from database import database
from apps import api


app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def startup():
    await database.disconnect()


app.include_router(api)
