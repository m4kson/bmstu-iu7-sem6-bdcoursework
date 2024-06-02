import datetime
from fastapi import Depends, HTTPException, status
import fastapi_users
from sqlalchemy import Table, Column, ForeignKey, Integer, Float, String, Date, Text, Enum, Boolean
from sqlalchemy.orm import relationship, Mapped, mapped_column, DeclarativeBase
from sqlalchemy.ext.declarative import declarative_base
import enum
from typing import Annotated, Literal
from fastapi_users.db import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy.ext.asyncio import AsyncSession
from app.session import get_db


Sex = Literal["м", "ж"]
Role = Literal["администратор", "оператор производства", "специалист по обслуживанию"]

class Base(DeclarativeBase):
    pass

class User(SQLAlchemyBaseUserTable[int], Base):
    """Base SQLAlchemy users table definition."""

    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    surname: Mapped[str]
    fatherame: Mapped[str]
    department: Mapped[str]
    dateofbirth: Mapped[datetime.date]
    sex:  Mapped[Sex] = mapped_column(Enum("м", "ж", name="sex_enum"))
    role:  Mapped[Role] = mapped_column(Enum("администратор", "оператор производства", "специалист по обслуживанию", name="role_enum"))


    email: Mapped[str] = mapped_column(String(length=320), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(length=1024), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

async def get_user_db(session: AsyncSession = Depends(get_db)):
    yield SQLAlchemyUserDatabase(session, User)
