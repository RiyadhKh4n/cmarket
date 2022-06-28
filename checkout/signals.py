"""
To listen for signals from OrderLineItem - when instance of this model
is saved or deleted. Then call the update_total method on the Order
instance that the lineitem relates to, so that the totals in the Order
instance get updated.
"""

from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver

from .models import OrderLineItem

@receiver(post_save, sender=OrderLineItem)
def update_on_save(sender, instance, created, **kwargs):
    """
    Update order total on lineitem update/create
    """
    instance.order.update_total()


@receiver(post_delete, sender=OrderLineItem)
def delete_on_save(sender, instance, **kwargs):
    """
    Update order total on lineitem delete
    """
    instance.order.update_total()
