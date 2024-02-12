from flask_wtf import FlaskForm
from wtforms import (
    BooleanField,
    FloatField,
    HiddenField,
    SelectField,
    StringField,
    SubmitField,
    TextAreaField,
)
from wtforms.validators import DataRequired


class CreateLead(FlaskForm):
    company = StringField("Company", validators=[DataRequired()])
    contact = StringField("Contact Name", validators=[DataRequired()])
    phone = StringField("Phone", validators=[DataRequired()])
    email = StringField("Email")
    contacted = BooleanField("Contacted", validators=[DataRequired()])
    converted = BooleanField("Converted", validators=[DataRequired()])
    hidden_field = HiddenField()
    l_submit = SubmitField("Submit")



class UpdateLead(FlaskForm):
    pass



class CreateClient(FlaskForm):
    is_lead = BooleanField("New Lead?")
    company = StringField("Company", validators=[DataRequired()])
    contact = StringField("Contact Name", validators=[DataRequired()])
    phone = StringField("Phone", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    submit = SubmitField("Submit")


class UpdateClient(FlaskForm):
    pass



class CreateProject(FlaskForm):
    company = SelectField("Company", validators=[DataRequired()])
    status = SelectField("Status", validators=[DataRequired()]) # choices will  be defined in route
    lead_selection = SelectField("Lead", validators=[DataRequired()])
    client_selction = SelectField("Client", validators=[DataRequired()])
    codename = StringField("Project Codename", validators=[DataRequired()])
    description = TextAreaField("Description", validators=[DataRequired()])
    hourly_rate = FloatField("Hourly Rate")
    total_hours = FloatField("Total Hours")
    wholesale = FloatField("Wholesale")

    submit = SubmitField("Create Project")


class ClockIn(FlaskForm):
    pass



class ClockOut(FlaskForm):
    pass
