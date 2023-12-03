from .extensions import db
from datetime import datetime

# this is from a combination of digital ocean and the flask-sqlalchemy docs
# digital ocean >> https://www.digitalocean.com/community/tutorials/how-to-use-flask-sqlalchemy-to-interact-with-databases-in-a-flask-application
# flask-sqlalchemy >> https://flask-sqlalchemy.palletsprojects.com/en/3.1.x/

# update the db declaration to include declarative base
# from sqlalchemy.orm import DeclarativeBase 

# class Base(DeclarativeBase):
#     pass

# db = SQLAlchemy(model_class=Base)


class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    f_name = db.Column(db.String(60), nullable=False)
    l_name = db.Column(db.String(60), nullable=True)
    phone = db.Column(db.String(15), nullable=False)
    email = db.Colum(db.String(100), nullable=False)

    def __repr__(self):
        return f"<Client {self.client}>"


class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    client = db.Column(db.String(120), unique=True, nullable=False)

    client_notes = db.relationship("ClientNotes", backref="client", lazy=True)

    def __repr__(self):
        return f"<Client {self.client}>"
        

class Industry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    industry = db.Column(db.String(100), unique=True)
    about_industry = db.Column(db.Text)

    companies = db.relationship("Company", backref="industry", lazy=True)

    def __repr__(self):
        return f"<Industry {self.industry}>"
    

class Company(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(100), nullable=False, unique=True)
    about_company = db.Column(db.Text)
    industry_id = db.Column(db.Integer, db.ForeignKey("industry.id"))


    def __repr__(self):
        return f"<Company {self.company}>"


class ClientNotes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    note_title = db.Column(db.String(100), nullable=False)
    note = db.Column(db.Text)
    client_id = db.Column(db.Integer, db.ForeignKey("client.id"))


    def __repr__(self):
        return f"<Client Note {self.title}>"


# usermixin ?
class ClientAccount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    contact_id = db.Column(db.Integer, db.ForeignKey("contact.id"))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    username = db.Column(db.String(60), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    recovery_email = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return f"<Client Account {self.client_account}>"


class ProjectStatus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    project_status = db.Column(db.String(100), nullable=False, unique=True)
    status_description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    projects = db.relationship("Project", backref="project_status", lazy=True)

    def __repr__(self):
        return f"<Project Status {self.project_status}>"


class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    status_id = db.Column(db.Integer, db.ForeignKey("project_status.id"))
    client_id = db.Colum(db.Integer, db.ForeignKey("client.id"))
    project = db.Column(db.String(100), unique=True,nullable=False)
    project_description = db.Column(db.Text)
    hourly_rate = db.Column(db.Real)
    total_hours = db.Column(db.Real)
    
    clock_ins = db.relationship("ClockIn", backref="project", lazy=True)
    tickets = db.relationship("Ticket", backref="project", lazy=True)    


    def __repr__(self):
        return f"<Project {self.project}>"


class TicketStatus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticket_status = db.Column(db.String(100), nullable=False, unique=True)
    status_description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    tickets = db.relationship("Ticket", backref="ticket_status", lazy=True)


    def __repr__(self):
        return f"<Ticket Status {self.ticket_status}>"


class Ticket(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    created_at = db.Column(db.DateTime, onupdate=datetime.utcnow)
    status_id = db.Column(db.Integer, db.ForeignKey("ticket_status.id"))
    project_id = db.Column(db.Integer, db.ForeignKey("project.id"))
    ticket = db.Column(db.String(100), nullable=False)
    ticket_description = db.Column(db.Text)

    ticket_items = db.relationship("TicketItem", backref="ticket", lazy=True)


    def __repr__(self):
        return f"<Ticket {self.ticket}>"



class TicketItem(db.Model):
    pass

    def __repr__(self):
        return f"<Ticket {self.ticket_item}>"

        
# and for __init__.py in the application factory

# with app.app_context():
#     db.create_all()