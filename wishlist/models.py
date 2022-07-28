from django.db import models
from products.models import Product
from django.contrib.auth.models import User


class FavouritesList(models.Model):
    """
    Class based model for storing users favourited items.
    """
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    product = models.ManyToManyField(
        Product,
        blank=True
    )
