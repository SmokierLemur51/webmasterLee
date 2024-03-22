"""
File: models.py
Author: Logan Lee

This file defines the models to be used in the web application.

List of leads and clients to populate at the end of the file.
"""
import datetime
from typing import List

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Boolean, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy.sql import func


class Base(DeclarativeBase):
    pass


db = SQLAlchemy(model_class=Base)

class LeadDiscoveryMethod(Base):
    """
    The method of discovery for a new lead. This will be great for future 
    lead targetting. 
    """
    __tablename__ = "lead_discovery_methods"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    method: Mapped[str] = mapped_column(String(120), nullable=False)
    method_description: Mapped[str] = mapped_column(String(255))

    leads: Mapped[List["Lead"]] = relationship(back_populates="discovery_method")

class Lead(Base):
    __tablename__ = "leads"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    discovery_method_id: Mapped[int] = mapped_column(ForeignKey("lead_discovery_methods.id"))
    company: Mapped[str] = mapped_column(String(100), nullable=True)
    name: Mapped[str] = mapped_column(String(100), nullable=True)
    email: Mapped[str] = mapped_column(String(100), nullable=True)
    phone: Mapped[str] = mapped_column(String(12), nullable=True)
    contacted: Mapped[bool] = mapped_column(Boolean, default=False)
    converted: Mapped[bool] = mapped_column(Boolean, default=False)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, default=func.now())
    contacted_at: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=True)
    comment: Mapped[str] = mapped_column(String(255), nullable=True)

    discovery_method: Mapped[LeadDiscoveryMethod] = relationship("LeadDiscoveryMethod", back_populates="leads")
    notes: Mapped[List["LeadNote"]] = relationship(back_populates="lead")

class LeadNote(Base):
    __tablename__ = "lead_notes"
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    lead_id: Mapped[int] = mapped_column(ForeignKey("leads.id"))
    note: Mapped[str] = mapped_column(String(255), nullable=False)
    content: Mapped[str] = mapped_column(String(500))

    lead: Mapped[Lead] = relationship("Lead", back_populates="notes")

class Client(Base):
    __tablename__ = "clients"

    id: Mapped[int] = mapped_column(primary_key=True)
    converted_from_lead: Mapped[bool] = mapped_column(Boolean, default=False)
    company: Mapped[str] = mapped_column(String(100), nullable=False)
    contact: Mapped[str] = mapped_column(String(100), nullable=False)
    phone: Mapped[str] = mapped_column(String(12), nullable=False)
    email: Mapped[str] = mapped_column(String(100))
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, default=func.now())

    projects: Mapped[List["Project"]] = relationship(back_populates="client")



class Status(Base):
    __tablename__ = "statuses"

    id: Mapped[int] = mapped_column(primary_key=True)
    _status: Mapped[str] = mapped_column(String(100), nullable=False)
    _description: Mapped[str] = mapped_column(String(250), nullable=False)

    projects: Mapped[List["Project"]] = relationship(back_populates="status")



class Project(Base):
    __tablename__ = "projects"

    id: Mapped[int] = mapped_column(primary_key=True)
    status_id: Mapped[int] = mapped_column(ForeignKey("statuses.id"), nullable=False)
    personal: Mapped[bool] = mapped_column(Boolean, nullable=False, default=False)
    client_id: Mapped[int] = mapped_column(ForeignKey("clients.id"))
    codename: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    project_description: Mapped[str] = mapped_column(String(500), nullable=False)
    hourly_rate: Mapped[float] = mapped_column(Float)
    total_hours_worked: Mapped[float] = mapped_column(Float)
    total_price: Mapped[float] = mapped_column(Float)

    status: Mapped[Status] = relationship(back_populates="projects")
    client: Mapped[Client] = relationship(back_populates="projects")
    
    tickets: Mapped[List["Ticket"]] = relationship(back_populates="project")


class Ticket(Base):
    __tablename__ = "tickets"

    id: Mapped[int] = mapped_column(primary_key=True)
    project_id: Mapped[int] = mapped_column(ForeignKey("projects.id"), nullable=False)
    status_id: Mapped[int] = mapped_column(ForeignKey("statuses.id"), nullable=False)
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(250), nullable=False)
    created_at: Mapped[datetime.datetime] = mapped_column(DateTime, default=func.now())
    completed_at: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=True)

    project: Mapped[Project] = relationship(back_populates="tickets")

