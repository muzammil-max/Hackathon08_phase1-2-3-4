import asyncio
from src.database import init_db
from src.models import User, Task, Session, Account, Verification # Ensure all models are registered
from src.database import engine
from sqlmodel import SQLModel

async def recreate_db():
    print("Dropping existing tables...")
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.drop_all)
    print("Initializing database...")
    async with engine.begin() as conn:
        await conn.run_sync(SQLModel.metadata.create_all)
    print("Database initialized successfully with Better Auth tables.")

if __name__ == "__main__":
    asyncio.run(recreate_db())