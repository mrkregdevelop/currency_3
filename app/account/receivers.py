from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver

from account.models import User


@receiver(pre_save, sender=User)
def lower_user_email(instance, **kwargs):
    instance.email = instance.email.lower()


@receiver(pre_save, sender=User)
def fix_user_phone(instance, **kwargs):
    pass


@receiver(post_save, sender=User)
def lower_user_email(instance, **kwargs):
    pass


'''
C - POST
R - GET
U - PUT/PATCH
D - DELETE
'''
