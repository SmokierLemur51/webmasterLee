from django.db import models


class DiscoveryMethod(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(255)


class ContactInformation(models.Model):
	first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    phone = models.CharField(max_length=10)
    email = models.CharField(max_length=120)


class Lead(models.Model):
	discovery_method = models.ForeignKey(DiscoveryMethod, on_delete=models.CASCADE)
	company = models.CharField(80)
	name = models.CharField(80)
	phone = models.CharField(10)
	email = models.CharField(120)
	facebook = models.BooleanField()
	google = models.BooleanField()
	contacted = models.BooleanField()
	converted = models.BooleanField()
	comment = models.TextField()


class LeadNote(models.Model):
	lead = models.ForeignKey(Lead, on_delete=models.CASCADE)
	title = models.CharField(120)
	note = models.TextField()


class Client(models.Model):
	discovery_method = models.ForeignKey(DiscoveryMethod, on_delete=models.CASCADE)
	main_contact = models.ForeignKey(ContactInformation, on_delete=models.CASCADE)
    all_contacts = models.ManyToMany
    company = models.CharField(80)
    
    

class ClientNote(models.Model):
	client = models.ForeignKey(Client, on_delete=models.CASCADE)
	title = models.CharField(120)
	note = models.TextField()

class ServiceOffer(models.Model):
	"""
	Services I offer, with prices attached.
	"""
	pass


class Proposal(models.Model):
	pass


class Project(models.Model):
	pass


class ProjectChecklist(models.Model):
	pass


class ProjectChecklistItem(models.Model):
	pass


class IssueTicket(models.Model):
	pass


class ClientReview(models.Model):
	"""
	Clients review projects, critique, request changes, or 
	give blessing to release into the wild.
	"""
	pass


class FinalOffer(models.Model):
	"""
	Upon completion of project, client reviews and is comfortable 
	with the final project. Make a final offer and connect contract.
	"""
	pass


class Subscription(models.Model):
	"""
	One to many relationship with Clients, and SubscriptionPaymentInformation.
	"""
	pass


class SubscriptionPaymentInformation(models.Model):
	"""
	Payment information with foreign key to subscription id.
	"""
	pass


class ServiceRequest(models.Model):
	"""
	How a client will request for upgrades or maintenance on a live product.
	"""
	pass


