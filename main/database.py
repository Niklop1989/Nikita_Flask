from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase
from uvicorn import Config
import aiosqlite
import psycopg2

DATABASE_URL = "postgresql+asyncpg://nik:nik@localhost:5432/nik"
# DATABASE_URL = "sqlite+aiosqlite:///./NNNNN.py.db"

# DATABASE_URL = "postgresql+psycopg2://nikit:nikit@localhost:5432/nikit"
engine = create_async_engine(DATABASE_URL, echo=True)
AsyncSessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=engine, class_=AsyncSession
)
Base = declarative_base()


async def get_db_session():
    async with AsyncSessionLocal() as session:
        yield session
