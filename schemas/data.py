from typing import Optional
from enum import Enum


from pydantic import BaseModel


class DataBase(BaseModel):
    station: str
    line: str
    amd_area: str
    district: str
    status: str
    i_d: str


class Data(DataBase):
    id: int


class CreateData(DataBase):
    id: Optional[int]


class ColumnName(str, Enum):
    id = 'id'
    station = 'station'
    line = 'line'
    amd_area = 'amd_area'
    district = 'district'
    status = 'status'
    i_d = 'i_d'


class SearchData(BaseModel):
    column: ColumnName
    value: str
