# https://pypi.org/project/quart-sqlalchemy/

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

from quart_sqlalchemy import SQLAlchemyConfig
from quart_sqlalchemy.framework import QuartSQLAlchemy


db = QuartSQLAlchemy()

class Client(db.Model):
    __tablename__ = "clients"

    id: Mapped[int] = mapped_column(sa.Identity(), primary_key=True, autoincrement=True)
    contact_id: Mapped[int]


class Project(db.Model):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(sa.Identity(), primary_key=True, autoincrement=True)
    status: Mapped[bool] = mapped_column(sa.Boolean, nullable=False, default=False)
    project_name: Mapped[str] = mapped_column(sa.String(100), nullable=False, unique=True)
    project_description: Mapped[str] = mapped_column(sa.String(500), nullable=False)
    client_id: Mapped[int] = mapped_column(sa.ForeignKey("clients.id"), )