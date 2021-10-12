from fastapi import APIRouter, HTTPException
from sqlalchemy import asc

from database import database
from models import data
from schemas import CreateData, Data, SearchData, ColumnName


api = APIRouter(prefix='/data', tags=['data'])


@api.get('/{id}', response_model=Data)
async def get(id: int):
    query = data.select().where(data.c.id == id)
    content = await database.fetch_one(query)
    if content is None:
        raise HTTPException(404)
    return content


@api.post('/add', response_model=CreateData)
async def post(get_data: CreateData):
    if isinstance(get_data.id, int):
        query = data.select().where(data.c.id == get_data.id)
        content = await database.fetch_one(query)
        if not(content is None):
            raise HTTPException(400)
    query = data.insert().values(
        **get_data.dict()
    )
    id_content = await database.execute(query)
    if get_data.id is None:
        get_data.id = id_content
        return get_data.dict()
    return get_data.dict()


@api.delete('/{id}', response_model=Data)
async def delete(id: int):
    query = data.select().where(data.c.id == id)
    content = await database.fetch_one(query)
    if content is None:
        raise HTTPException(404)
    queue = data.delete().where(data.c.id == id)
    return await database.execute(queue)


@api.get('/list/{page}/{limit}', response_model=list[Data])
async def get_all(page: int, limit: int):
    query = data.select().order_by(
        asc(data.c.station)
    ).limit(limit).offset(page)
    return await database.fetch_all(query)


@api.post('/search', response_model=list[Data])
async def get_search(page: int, limit: int, searches: list[SearchData]):
    query = data.select()
    for search in searches:
        match search.column:
            case ColumnName.id:
                query = query.where(data.c.id.like(search.value+"%"))
            case ColumnName.station:
                query = query.where(data.c.station.like(search.value+"%"))
            case ColumnName.line:
                query = query.where(data.c.line.like(search.value+"%"))
            case ColumnName.amd_area:
                query = query.where(data.c.amd_area.like(search.value+"%"))
            case ColumnName.district:
                query = query.where(data.c.district.like(search.value+"%"))
            case ColumnName.station:
                query = query.where(data.c.station.like(search.value+"%"))
            case ColumnName.i_d:
                query = query.where(data.c.i_d.like(search.value+"%"))
        print(query)
    query.limit(limit).offset(page)
    return await database.fetch_all(query)
