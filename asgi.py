import os

from get_csv import get_csv

get_csv()

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(
        'main:app',
        log_config=os.environ['LOGGER_CONFIG'],
    )
