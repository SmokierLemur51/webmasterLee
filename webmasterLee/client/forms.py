from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField,SubmitField 
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError


class CreateNewProjectRequest(FlaskForm):
	project_name = StringField("Project Name", validators=[DataRequired])
	description = TextAreaField("Describe Project", validators=[DataRequired])




