"""
File: tests/leads.py

For populating database with test leads, as well as sorting out bugs & issues. 

Author: Logan Lee

class Lead(Base):
    __tablename__ = "leads"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    company: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(100))
    email: Mapped[str] = mapped_column(String(100))
    phone: Mapped[str] = mapped_column(String(12), nullable=False)
    contacted: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    converted: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, default=func.now())
    contacted_at: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=True)
    comment: Mapped[str] = mapped_column(String(255))

"""
from ..models import Lead

# Leads listed concurrent with 17-March-2024
leads = [
    Lead(
        company="Harper Audo Productions", name="Roderick Harper",
        phone="5027241192", 
        comment="Reffered through Callie, already has website but is unhappy I think... harperaudioproductions.com",
        ), 
    Lead(
        company="Bluegrass Gutters", phone="5029754526",
        ),
    Lead(
        company="Masden Concrete & Hauling", phone="5026485997",
        comment="Billy from Lansing's fathers company",
        ),
    Lead(
        company="Tipton Construction & Home Improvement", phone="3177174810",
        email="anthonytipton@gmail.com",
        ),
    Lead(
        company="Thrasher Improvements", phone="5028021437", name="Jason",
        ),
    Lead(
        company="SC General Contracting", phone="5023869308",
        ),
    Lead(
        company="", phone="",
        ),
]
