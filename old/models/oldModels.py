from datetime import date
from old import db
from flask_login import UserMixin


''' ~~ ~~ TMS SECTION ~~ ~~ '''

class Ticket(db.Model):
	__tablename__ = "tickets"
	id = db.Column(db.Integer, primary_key=True)
	date_created = db.Column(db.Date, nullable=False, default=date.today)
	title = db.Column(db.String(100), nullable=False, unique=True)
	description = db.Column(db.String(250), nullable=False)
	complete = db.Column(db.Boolean, default=False)
	personal = db.Column(db.Boolean, nullable=False) 
	tasks = db.relationship("Tasks", backref="ticket", lazy=True,)

	# when not personal create timeclock to go in conjunction with it
	# if self.personal is False:


class Tasks(db.Model):
	__tablename__ = "tasks"
	id = db.Column(db.Integer, primary_key=True)
	date_created = db.Column(db.Date, nullable=False, default=date.today)
	complete = db.Column(db.Boolean, default=False)
	title = db.Column(db.String(100), nullable=False)
	description = db.Column(db.String(250), nullable=False)
	ticket_id = db.Column(db.Integer, db.ForeignKey("tickets.id"), nullable=False)
	subtasks = db.relationship("Subtask", backref="task", lazy=True,)


class SubTask(db.Model):
	__tablename__ = "subtasks"
	id = db.Column(db.Integer, primary_key=True)
	date_created = db.Column(db.Date, nullable=False, default=date.today) 
	complete = db.Column(db.Boolean, default=False)
	title = db.Column(db.String(100), nullable=False)
	description = db.Column(db.String(250), nullable=False)
	task_id = db.Column(db.Integer, db.ForeignKey("tasks.id"), nullable=False)


''' ~~ ~~ FINANCES SECTION ~~ ~~ '''

# class SpendingCategory(db.Model):


class Category(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	category = db.Column(db.String(120), unique=True, nullable=False)
	description = db.Column(db.String(500), nullable=False)
	locations = db.relationship("Location", backref='reciever', lazy=True)


class Location(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(120), unique=True, nullable=False)
	category = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)
	visits = db.relationship("Visit", backref="location", lazy=True)

	@property
	def total_spent(self):
		total = 0
		for visit in self.visits:
			total += visit.expense # i think i am trying to do the wrong thing here
		return total

	def update_total_spent(self):
		self.total_spent = sum(visit.expense for visit in self.visits)


class Visit(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	date = db.Column(db.Date, nullable=False)
	location = db.Column(db.Integer, db.ForeignKey("location.id"), nullable=False)
	expense = db.relationship("Expense", uselist=False, backref="visit", lazy=True)


class Expense(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	date = db.Column(db.Date, nullable=False)
	amount = db.Column(db.Numeric(precision=10, scale=2), nullable=False) 


