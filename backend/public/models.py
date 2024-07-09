from django.db import models
from django.utils import timezone


class StatusCode(models.Model):
    status = models.CharField(max_length=100)
    info = models.CharField(max_length=250)

    def __str__(self):
        return self.status


class ContactRequest(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, )
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=12)
    email = models.EmailField(max_length=120)
    message = models.CharField(max_length=500)
    
    def __str__(self):
        return self.name


class ContactRequestNote(models.Model):
    contact_request = models.ForeignKey("ContactRequest", on_delete=models.CASCADE) 
    note = models.CharField(max_length=250)


class PortfolioProject(models.Model):
    codename = models.CharField(max_length=120)
    url = models.URLField(max_length=500)
    about = models.TextField()