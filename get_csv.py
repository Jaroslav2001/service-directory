import os
from csv import reader
import asyncio
from database import database
from models import data
from schemas import CreateData

content: list[list[str]] = []


async def set_database():
    await database.connect()
    global content
    new_content: list[list[str]] = []
    for line in content:
        new_content += [line[0].split(';')]
    contents: [dict] = []
    for list_content in new_content:
        contents.append(CreateData(
            station=list_content[0],
            line=list_content[1],
            amd_area=list_content[2],
            district=list_content[3],
            status=list_content[4],
            i_d=list_content[5]
        ).dict())
    query = data.insert().values(
        **contents[0]
    )
    await database.execute_many(query=query, values=contents)
    await database.disconnect()


def get_csv():
    global content
    with open(os.environ['FILE_CSV'], 'r') as file:
        content = reader(file)
        asyncio.run(set_database())
