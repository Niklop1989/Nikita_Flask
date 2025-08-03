import asyncio
from contextlib import asynccontextmanager

import uvicorn
from fastapi import FastAPI, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from database import engine, get_db_session
from schema import ProductAddPost, UserAddPost
from models import Base, Product, User

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Hello, World!"}


@app.post("/")
async def setup_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)
    return {'ok': 200}



# @app.post("/")
# async def setup_database():
#     await Base.metadata.create_all(engine)
#     return {'ok': 200}


@app.post('/user', )
async def recipes(prod: UserAddPost, session: AsyncSession = Depends(get_db_session)):
    new_recipes = User(
        first_name=prod.first_name,
        second_name=prod.second_name,
        birth_date=prod.birth_date,
        age=prod.age,
        address=prod.address,
        country=prod.country
    )
    session.add(new_recipes)
    await session.commit()
    return {"ok": True}


@app.post('/product', )
async def recipes(prod: ProductAddPost, session: AsyncSession = Depends(get_db_session)):
    new_recipes = Product(
        title=prod.title,
        description=prod.description,
        price=prod.price,
        user_id=prod.user_id
    )
    session.add(new_recipes)
    await session.commit()
    return {"ok": True}


@app.get('/user')
async def get_products_handler(session: AsyncSession = Depends(get_db_session)):
    res = await session.execute(select(User).order_by(User.first_name.desc(),
                                                      User.first_name.desc()))
    return res.scalars().all()


if __name__ == '__main__':
    # uvicorn.run("main:app", host='0.0.0.0')
    uvicorn.run("main:app", host="0.0.0.0", port=8000)
