"""
File: blueprints/portal/leads.py

Functions to operate on leads.

Author: Logan Lee
"""
from flask_sqlalchemy import SQLAlchemy

from ...models import db, Client, Lead


def get_method_id(method: str, method_list: list) -> int:
    # i think you can delete this
    for m in method_list:
        if m[1] == method:
            return m[0]


def convert_lead_client(db: SQLAlchemy, lead: Lead) -> Client:
    """
    Open database transaction, convert lead notes into client notes,
    mark lead as converted, create new Client entry, and commit changes.
    """
    # start database transaction

    # mark lead as converted
    
    # load all notes

    # create, commit changes & return new client
    return Client()


def create_project_proposal() -> None:
    pass
