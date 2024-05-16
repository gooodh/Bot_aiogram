import os
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from database.models import Base

from config import DB_URL, db_lite
from common.texts_for_db import categories, description_for_info_pages
from database.orm_query import orm_add_banner_description, orm_create_categories


#from .env file:
# DB_LITE=sqlite+aiosqlite:///my_base.db
# DB_URL=postgresql+asyncpg://login:password@localhost:5432/db_name

engine = create_async_engine(db_lite, echo=True)

# engine = create_async_engine(DB_URL, echo=True)

session_maker = async_sessionmaker(bind=engine, class_=AsyncSession,
                                   expire_on_commit=False)


async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        
    async with session_maker() as session:
        await orm_create_categories(session, categories)
        await orm_add_banner_description(session, description_for_info_pages)


async def drop_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
