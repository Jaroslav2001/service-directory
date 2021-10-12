from sqlalchemy import Table, Column, Integer, String

from database import metadata


data = Table(
    "data",
    metadata,
    Column('id', Integer, primary_key=True),
    Column('station', String),
    Column('line', String),
    Column('amd_area', String),
    Column('district', String),
    Column('status', String),
    Column('i_d', String),
)
