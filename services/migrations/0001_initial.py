# Generated by Django 3.1 on 2020-10-05 10:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MailList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staff_code', models.CharField(max_length=40)),
                ('DOB', models.DateField(default=django.utils.timezone.now, null=True)),
                ('address', models.TextField(default='Not stated')),
                ('job_title', models.CharField(max_length=50)),
                ('last_updated', models.DateTimeField(auto_now_add=True)),
                ('registration_date', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Not available', max_length=50, null=True)),
                ('phone_no', models.CharField(max_length=20)),
                ('home_address', models.TextField(default='Not available')),
                ('DOB', models.DateField(default=django.utils.timezone.now, null=True)),
                ('social_media', models.CharField(default='Not available', max_length=200, null=True)),
                ('last_updated', models.DateTimeField(auto_now_add=True)),
                ('registration_date', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BusinessOwner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_no', models.CharField(default='Not available', max_length=20, null=True)),
                ('company_name', models.CharField(default='Not available', max_length=50)),
                ('company_address', models.TextField()),
                ('service_title', models.CharField(default='Not available', max_length=50)),
                ('service_description', models.TextField(default='Not available')),
                ('CAC_code', models.CharField(default='Not available', max_length=20, null=True)),
                ('guarantors_name', models.CharField(default='Not available', max_length=50)),
                ('guarantor_phone_no', models.CharField(default='Not available', max_length=20)),
                ('guarantors_address', models.TextField(default='Not available')),
                ('last_updated', models.DateTimeField(auto_now_add=True)),
                ('registration_date', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
