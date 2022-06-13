from django.db import models
from django.contrib.auth.models import User


class Newsletter(models.Model):
    """
    Class that defines the Newsletter model
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=254)
    accept_policy = models.BooleanField(default=False)


class ContactForm(models.Model):
    """
    Class that defines the ContactForm model
    """
    email = models.EmailField(max_length=254)
    details = models.TextField()
