from django.db import models
from products.models import Product
from django.contrib.auth.models import User


class Wishlist(models.Model):
    """
    Class for the Wishlist model
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)