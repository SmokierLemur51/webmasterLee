from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class CreateTicketForm(FlaskForm):
	title = StringField("Title", validators=[DataRequired()])
	description = TextAreaField("Description", validators=[DataRequired()])
	personal = BooleanField("Personal Project?")
	submit = SubmitField("Create Ticket")


class CreateTicketTasksForm(FlaskForm):
	title = StringField("Task", validators=[DataRequired()])
	description = TextAreaField("Description", validators=[DataRequired()])
	submit = SubmitField("Add Task to Ticket")


class UpdateTicketSubTasksForm(FlaskForm):
	title = StringField("Todo", validators=[DataRequired()])
	description = TextAreaField("Description", validators=[DataRequired()])
	submit = SubmitField("Create Task Todo Item")

