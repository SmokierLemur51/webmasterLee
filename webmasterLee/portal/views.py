from flask import Blueprint, render_template, current_app
from ..extensions import db

portal = Blueprint("portal", __name__, template_folder="templates")



@portal.route("/")
def index():
	elements = {
		"title": "Welcome Guru",
	}
	return render_template("portal-index.html", elements=elements)



@portal.route("/tickets")
def tickets():

	return render_template("tickets.html")


# - - - - - - - - - - - - - - - - - - - - - - - - -
# - - - - - - - - Form Processing - - - - - - - - -
# - - - - - - - - - - - - - - - - - - - - - - - - -



''' Temporary Testing Variables '''
# tickets = {
# 	"incomplete": [{
# 			"title": "testing 1",
# 			"start": date.today(),
# 			"content": ["this is the content",],
# 		},{
# 			"title": "second test",
# 			"start": date.today(),
# 			"content": ["testing the list", "for this there is a lot to do", "keep going you can do it"],
# 		},],
# 	"complete": [
# 		{
# 			"title": "first completed",
# 			"end": date.today(),
# 			"content": ["completed content",]
# 		}],

# }

''' ROUTES '''

# @guru.route("/tms")
# def tms_index():

# 	return render_template("tms/tms_index.html", tickets=tickets)


# @guru.route("/tms/manage")
# def tms_manage_ticket():
# 	''' This will act as the main tickets page '''

# 	return render_template("tms/tms_manage.html",)



# @guru.route("/tms/create/ticket", methods=["GET", "POST"])
# def tms_create_ticket():
# 	ticket_form = CreateTicketForm()	
# 	if ticket_form.validate_on_submit():
# 		ticket = Ticket(
# 			title=ticket_form.title.data,
# 			description=ticket_form.description.data,
# 			date=date.today(),
# 			personal=ticket_form.personal.data,
# 		)
# 		db.session.add(ticket)
# 		db.session.commit()
# 		return redirect(url_for("tms_index"))
# 	return render_template("tms/tms_create.html", form=ticket_form)


# @guru.route("/tms/create/<ticket>")
# def tms_manage__this_ticket(ticket, ticket_id):
# 	return None

# @guru.route("/tms/progress")
# def tms_view_progress():



# 	return render_template("tms/tms_progress.html", context=context)

