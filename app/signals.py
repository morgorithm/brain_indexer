from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Category, Card

@receiver(post_save, sender=Card)
def cardPostSave(sender, **kwargs) :
    if kwargs['created'] :
        category = kwargs['instance'].category
        category.total += 1
        category.save()

@receiver(post_delete, sender=Card)
def cardPostDelete(sender, **kwargs) :
    category = kwargs['instance'].category
    category.total -= 1
    category.save()