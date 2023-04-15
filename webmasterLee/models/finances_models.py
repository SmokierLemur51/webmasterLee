from datetime import datetime
from greenleaf import db, login_manager
from flask_login import UserMixin


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
			total += visit.payment
		return total

	def update_total_spent(self):
		self.total_spent = sum(visit.payment for visit in self.visits)


class Visit(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	date = db.Column(db.Date, nullable=False)
	location = db.Column(db.Integer, db.ForeignKey("location.id"), nullable=False)
	payment = db.relationship("Payment", uselist=False, backref="visit", lazy=True)


class Payment(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	date = db.Column(db.Date, nullable=False)
	amount = db.Column(db.Numeric(precision=10, scale=2), nullable=False) 


'''

class Payment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Numeric(precision=10, scale=2), nullable=False)
    visit_id = db.Column(db.Integer, db.ForeignKey('visit.id'), nullable=False)


== == == == == == == == == == == == 

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    visits = db.relationship('Visit', backref='restaurant', lazy=True)
	
    @property
    def num_visits(self):
        return len(self.visits)

    def total_spent(self):
        return sum(visit.spent for visit in self.visits)

class Visit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    spent = db.Column(db.Float, nullable=False)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
'''

