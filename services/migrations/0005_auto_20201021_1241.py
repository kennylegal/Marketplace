# Generated by Django 3.1 on 2020-10-21 11:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0004_comment_to'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='to',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='services.businessowner'),
        ),
    ]