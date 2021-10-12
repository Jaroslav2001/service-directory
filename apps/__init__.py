from fastapi import APIRouter

from . import data


api = APIRouter(prefix='/api')
api.include_router(data.api)
