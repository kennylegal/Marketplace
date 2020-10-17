from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True, default='Not available')
    phone_no = models.CharField(max_length=20)
    home_address = models.TextField(default='Not available')
    DOB = models.DateField(null=True, default=timezone.now)
    social_media = models.CharField(max_length=200, null=True, default='Not available')
    last_updated = models.DateTimeField(auto_now_add=True)
    registration_date = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.user)


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    staff_code = models.CharField(max_length=40)
    DOB = models.DateField(null=True, default=timezone.now)
    address = models.TextField(default='Not stated')
    job_title = models.CharField(max_length=50)
    last_updated = models.DateTimeField(auto_now_add=True)
    registration_date = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.user)


class BusinessOwner(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_no = models.CharField(max_length=20, null=True, default='Not available')
    company_name = models.CharField(max_length=50, default='Not available')
    company_address = models.TextField()
    service_title = models.CharField(max_length=50, default='Not available')
    service_description = models.TextField(default='Not available')
    CAC_code = models.CharField(null=True, max_length=20, default='Not available')
    guarantors_name = models.CharField(max_length=50, default='Not available')
    guarantor_phone_no = models.CharField(max_length=20, default='Not available')
    guarantors_address = models.TextField(default='Not available')
    last_updated = models.DateTimeField(auto_now_add=True)
    registration_date = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return str(self.user)


class MailList(models.Model):
    email = models.CharField(max_length=50)

    def __str__(self):
        return str(self.email)
