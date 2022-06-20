from django.db import models
from django.contrib.auth.models import User


class Newsletter(models.Model):
    """
    Class that defines the Newsletter model
    """
    email = models.EmailField(max_length=254, blank=False, null=False)
    accepted_privacy_policy = models.BooleanField(default=False,
                                                  blank=False, null=False)
    registered_user = models.ForeignKey(
                User, on_delete=models.SET_NULL, blank=True, null=True,
                related_name='newsletter_subscriber')
    created_on = models.DateTimeField(auto_now=True, editable=False)
    updated_on = models.DateTimeField(auto_now=True, editable=False)


class ContactForm(models.Model):
    """
    Class that defines the ContactForm model
    """
    email = models.EmailField(max_length=254)
    details = models.TextField()
