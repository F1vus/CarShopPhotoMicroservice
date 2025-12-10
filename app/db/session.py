from __future__ import annotations

from typing import AsyncGenerator, Optional

from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)
from sqlalchemy.orm import declarative_base

from app.config import config


class SessionManager:
    """Manages asynchronous DB sessions with connection pooling."""

    def __init__(self) -> None:
        self.engine: Optional[AsyncEngine] = None
        self.session_factory: Optional[async_sessionmaker[AsyncSession]] = None

    def init_db(self) -> None:
        connect_args = {}

        self.engine = create_async_engine(
            config.postgres_dsn,
            echo=config.postgres_echo,
            pool_pre_ping=True,
            connect_args=connect_args,
        )

        self.session_factory = async_sessionmaker(
            self.engine,
            expire_on_commit=False,
            autoflush=False,
            class_=AsyncSession,
        )

    async def close(self) -> None:
        """Dispose of the database engine."""
        if self.engine:
            await self.engine.dispose()
            
    async def get_db(self) -> AsyncGenerator[AsyncSession, None]:
        """Yield a database session with the correct schema set."""
        if not self.session_factory:
            raise RuntimeError("Database session factory is not initialized.")

        async with self.session_factory() as session:
            try:
                yield session
            except:
                await session.rollback()
                raise


# Global instances
sessionmanager = SessionManager()
Base = declarative_base()

