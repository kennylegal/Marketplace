from django.db.models.signals import post_save
from django.contrib.auth.models import User, Group
from .models import *
from django.dispatch import receiver


@receiver(post_save, sender=User)
def customer_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='customer')
        instance.groups.add(group)
        Customer.objects.create(
            user=instance,
            name=instance.username
    )
        print('profile created')
    elif created == False:
        instance.customer.save()
        print('profile updated')


@receiver(post_save, sender=User)
def businessOwner(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='businessOwner')
        instance.groups.add(group)
        BusinessOwner.objects.create(
            user=instance,
        )
        print('Your profile has been created successfully')
    elif not created:
        instance.businessowner.save()
        print('Your profile has been updated')

#
# @receiver(post_save, sender=User)
# def staff(sender, instance, created, **kwargs):
#     if created:
#         group = Group.objects.get(name='staff')
#         instance.groups.add(group)
#         Staff.objects.create(
#             user=instance,
#         )
#         print('Your staff profile has been created successfully')
#     elif not created:
#         instance.staff.save()
#         print('Your staff profile has been updated')
