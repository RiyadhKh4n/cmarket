from django.db import models
from django.contrib.auth.models import User


class Newsletter(models.Model):
    email = models.EmailField()
    subscribed_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """newsletter meta class"""
        ordering = ['subscribed_on']
        verbose_name_plural = 'Subscriptions'

    def __str__(self):
        return self.email


class ContactForm(models.Model):
    email = models.EmailField()
    subject = models.CharField(max_length=255, blank=True)
    message = models.TextField()

    def __str__(self):
        return self.email
