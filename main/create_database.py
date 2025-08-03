import json

from sqlalchemy import insert

from database import engine

def load_data(file_path):
    with open(file_path,'r')as file:
        return json.load(file)

async def create(table,data):
    async with engine.connect()as conn:
        await conn.execute(insert(table),data)
        await conn.commit()

async def main():
    pass

