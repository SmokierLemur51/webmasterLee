# https://pypi.org/project/quart-sqlalchemy/

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from quart_sqlalchemy import SQLAlchemyConfig
from quart_sqlalchemy.framework import QuartSQLAlchemy


db = QuartSQLAlchemy(
    config=SQLAlchemyConfig(
        binds=dict(
            default=dict(
                url="sqlite///",
                echo=True,
                connect_args=dict(check_same_threads=False)
            ),
            session=dict(
                expire_on_commit=False,
            ),
        )
    ),
)

class Project(db.Model):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(sa.Identity(), primary_key=True, autoincrement=True)
    status: Mapped[bool] = mapped_column(sa.Boolean, nullable=False, default=False)
    project_name: Mapped[str] = mapped_column(sa.String(100), nullable=False, unique=True)
    project_description: Mapped[str] = mapped_column(sa.String(500), nullable=False)
    customer: Mapped[int] = mapped_column(sa.ForeignKey("customer.id"), )