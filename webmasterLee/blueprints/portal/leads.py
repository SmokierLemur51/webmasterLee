"""
File: blueprints/portal/leads.py

Functions to operate on leads.

Author: Logan Lee
"""
from ...models import db, Client, Lead


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
