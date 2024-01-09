# https://pypi.org/project/quart-sqlalchemy/
import datetime
from typing import List

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Boolean, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.sql import func

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)


class Client(Base):
    __tablename__ = "clients"

    id: Mapped[int] = mapped_column(Identity(), primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(60), nullable=False, unique=True)
    phone: Mapped[str] = mapped_column(String(12), nullable=False, unique=True)
    name: Mapped[str] = mapped_column(String(40), nullable=False)


class ClientAccount(Base):
    __tablename__ = "client_accounts"

    id: Mapped[int] = mapped_column(Identity(), primary_key=True, autoincrement=True)
    email: Mapped[str] = mapped_column(String(60), nullable=False, unique=True)
    phone: Mapped[str] = mapped_column(String(12), nullable=False, unique=True)
    name: Mapped[str] = mapped_column(String(40), nullable=False)

class Project(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(sa.Identity(), primary_key=True, autoincrement=True)
    status: Mapped[bool] = mapped_column(sa.Boolean, nullable=False, default=False)
    project_name: Mapped[str] = mapped_column(sa.String(100), nullable=False, unique=True)
    project_description: Mapped[str] = mapped_column(sa.String(500), nullable=False)
    client_id: Mapped[int] = mapped_column(sa.ForeignKey("clients.id"))

