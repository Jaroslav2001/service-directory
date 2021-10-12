from sqlalchemy import create_engine

from database import DATABASE_URL
from models import metadata


if __name__ == '__main__':
    engine = create_engine(
        DATABASE_URL
    )
    metadata.drop_all(engine)
    metadata.create_all(engine)
