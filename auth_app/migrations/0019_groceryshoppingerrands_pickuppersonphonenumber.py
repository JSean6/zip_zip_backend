# Generated by Django 5.0.6 on 2025-01-21 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0018_groceryshoppingerrands'),
    ]

    operations = [
        migrations.AddField(
            model_name='groceryshoppingerrands',
            name='pickupPersonPhoneNumber',
            field=models.IntegerField(null=True),
        ),
    ]
