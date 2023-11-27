from flask_wtf import FlaskForm
from wtforms import (
    StringField, SubmitField, FloatField,
    BooleanField, TextAreaField, SelectField,
	MultipleFileField,
)    

from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

class LoginForm(FlaskForm):
	pass

class CreateTicketForm(FlaskForm):
	title = StringField(label="Title", validators=[DataRequired()])
	description = TextAreaField(label="Description", validators=[DataRequired()])
	personal = BooleanField(label="Personal Project?")
	submit = SubmitField(label="Create Ticket")


class CreateTicketTasksForm(FlaskForm):
	title = StringField(label="Task", validators=[DataRequired()])
	description = TextAreaField(label="Description", validators=[DataRequired()])
	submit = SubmitField(label="Add Task to Ticket")


class UpdateTicketSubTasksForm(FlaskForm):
	title = StringField(label="Todo", validators=[DataRequired()])
	description = TextAreaField(label="Description", validators=[DataRequired()])
	submit = SubmitField(label="Create Task Todo Item")


class CreateProjectForm(FlaskForm):
	project_status = SelectField(label="Status", choices=[], )
	client_id = SelectField()
	title = StringField(label="Project Name", validators=[DataRequired()])
	content = TextAreaField(label="Description", validators=[DataRequired()])
	hourly_rate = FloatField()
	total_hours = FloatField()
	customer_files = MultipleFileField()



